# DSA2000 Fiber Receiver

This repository contains the hardware design for the RF over fiber receiver module.
This module provides the data center-local analog signal processing following the conversion of optical to RF with a photodiode.
It is designed to interface with the "Radio Camera Frontend" card, and hence uses board-to-board connectors for the digital control and RF output.
Additionally, this module provides several monitor and control points that will eventually be integrated into the telescope's global monitor and control system.

## Hardware

Designed using KiCad 9, and requires setup of our [library](https://gitlab.com/dsa-2000/asp/kicad-library).

### Artifacts

As part of the CI/CD pipeline for this project, schematics, board files, BoMs, etc. are rendered on each change.
You can find the latest artifacts [here](https://gitlab.com/dsa-2000/asp/rfof/frx/-/jobs/artifacts/main/browse?job=artifacts)

