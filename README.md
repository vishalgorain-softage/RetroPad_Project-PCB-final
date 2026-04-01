# RetroPad PCB Design using SKiDL

## Overview

This project demonstrates a complete hardware design workflow using SKiDL (a Python-based electronic design library) and KiCad (an open-source PCB design tool). The objective is to programmatically define a circuit, generate a netlist, and prepare it for PCB implementation in a structured and reproducible manner.

---

## Methodology: Circuit Design and PCB Development via SKiDL–KiCad Pipeline

The project follows a systematic pipeline that converts a Python-defined circuit into a manufacturable PCB layout. This approach ensures modularity, clarity in connectivity, and consistency across the design process.

---

### Per-Component Circuit Definition

Each circuit element is defined programmatically using SKiDL. Components are instantiated in Python to ensure uniformity and scalability.

The implemented components include:

* Resistors
  Used for current limiting and signal stabilization. Example values include 330Ω (LED current limiting) and 10kΩ (pull-down configuration).

* LED (Light Emitting Diode)
  Functions as a visual output indicator within the circuit.

* Push Button Switch
  Serves as an input mechanism. Each switch is paired with a pull-down resistor to maintain stable logic levels.

* Capacitor (0.1µF)
  Used for decoupling and noise suppression between the power (VCC) and ground (GND) lines.

* Connector (Pin Header)
  Provides an interface for external systems such as a microcontroller or input/output connections.

Each component is treated as an independent logical unit, enabling modular design and easier expansion.

---

### Circuit Construction Strategy

The overall circuit is constructed using global power nets:

* VCC (power supply)
* GND (ground reference)

All components are interconnected through clearly defined signal nets. Input signals from push buttons and output signals to the LED are routed through these nets. A connector interface is used to link the circuit with external hardware, ensuring flexibility and scalability.

---

### Netlist Generation Pipeline

The SKiDL script processes the circuit definition and generates standard output files:

* `.net` file for PCB design integration
* `.xml` file for structured circuit representation

An Electrical Rule Check (ERC) is performed to validate the circuit. This ensures there are no floating nodes, missing connections, or electrical conflicts. The generated files act as the bridge between logical design and physical PCB implementation.

---

### PCB Layout Implementation

The generated netlist is imported into KiCad’s PCB Editor. Components are assigned appropriate footprints and placed according to the intended layout.

The placement strategy follows a logical grouping of components to reflect functional relationships, improving readability and usability of the design.

---

### Layout and Routing Strategy

Component placement is optimized to maintain clarity and reduce routing complexity. Electrical connections are completed through trace routing while ensuring:

* Minimal trace overlap
* Clean and direct signal paths
* Proper grounding strategy

Optional ground planes can be used to improve signal integrity and reduce electrical noise.

---

### Validation and Design Checks

The PCB design is verified using Design Rule Checks (DRC) within KiCad. This ensures:

* Manufacturability of the PCB
* Correct electrical connectivity
* Consistency with the generated netlist

Any inconsistencies are resolved through iterative refinement of the design.

---

### Dependency and Environment Management

The project uses:

* Python with the SKiDL library for circuit generation
* KiCad for schematic verification and PCB layout

All dependencies are managed within a virtual environment to ensure reproducibility and avoid configuration conflicts across different systems.

---

## Project Files

The repository includes the following key files:

* `main.py` — SKiDL source code defining the circuit
* `final.net` — Generated netlist used for PCB design
* `retropad.net` — Reference netlist for comparison
* `report.txt` — Supporting documentation

---

## Result

The project successfully demonstrates:

* Programmatic circuit design using SKiDL
* Generation of a valid netlist
* Compatibility with KiCad for PCB implementation
* A modular and reproducible hardware design workflow

---

## Author

Vishal Gorain

---

## Status

Completed. Netlist successfully generated and ready for PCB design and verification.
