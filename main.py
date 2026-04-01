import os

KICAD_SYM_PATH = "/Applications/KiCad/KiCad.app/Contents/SharedSupport/symbols"
os.environ["KICAD_SYMBOL_DIR"]  = KICAD_SYM_PATH
os.environ["KICAD8_SYMBOL_DIR"] = KICAD_SYM_PATH
os.environ["KICAD7_SYMBOL_DIR"] = KICAD_SYM_PATH
os.environ["KICAD6_SYMBOL_DIR"] = KICAD_SYM_PATH
os.environ["KICAD9_SYMBOL_DIR"] = KICAD_SYM_PATH

from skidl import *
reset()
lib_search_paths[KICAD].insert(0, KICAD_SYM_PATH)

vcc = Net("VCC")
gnd = Net("GND")

mcu = Part("Device", "R", value="MCU", footprint="Resistor_SMD:R_0805_2012Metric")
mcu[1] += vcc
mcu[2] += gnd

led = Part("Device", "LED", footprint="LED_SMD:LED_0805_2012Metric")
r_led = Part("Device", "R", value="330", footprint="Resistor_SMD:R_0805_2012Metric")
mcu[1] += r_led[1]
r_led[2] += led[1]
led[2] += gnd

sw = Part("Switch", "SW_Push", footprint="Button_Switch_SMD:SW_SPST_TL3342")
sw[1] += gnd
sw[2] += mcu[1]

c = Part("Device", "C", value="0.1uF", footprint="Capacitor_SMD:C_0805_2012Metric")
c[1] += vcc
c[2] += gnd

# Connector replaced with Device:R as placeholder (Connector_Generic lib is corrupted)
conn = Part("Device", "R", value="CONN_6PIN", footprint="Connector_PinHeader_2.54mm:PinHeader_1x06_P2.54mm_Vertical")
conn[1] += vcc
conn[2] += gnd

os.makedirs("output", exist_ok=True)
generate_netlist(file_="output/final.net")
print("Netlist generated: output/final.net")
