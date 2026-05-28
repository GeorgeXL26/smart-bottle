# RP2350-Plus — English Spec Sheet

> Translated from [Waveshare Wiki (Chinese)](https://www.waveshare.net/wiki/RP2350-Plus)

## Product Overview

The RP2350-Plus is an enhanced version of the Raspberry Pi Pico 2 based on the RP2350 microcontroller. It is compatible with most Pico 2 modules while adding extra features.

## Specifications

| Item | Detail |
|------|--------|
| **MCU** | RP2350A — dual-core, dual-architecture |
| **Cores** | 2× ARM Cortex-M33 + 2× Hazard 3 RISC-V @ 150MHz |
| **SRAM** | 520 KB |
| **Flash** | 4 MB onboard |
| **USB Connector** | USB Type-C |
| **Battery** | Onboard LiPo charge/discharge interface |
| **Power IC** | MP28164 DC-DC buck-boost, up to 2A load |
| **Form Factor** | Castellation holes for direct soldering |
| **USB Support** | USB 1.1 host and device |
| **Low Power** | Sleep and deep sleep modes |
| **Programming** | Drag-and-drop via mass storage (UF2) |
| **GPIO** | 26 multifunctional pins |
| **SPI** | 2 |
| **I2C** | 2 |
| **UART** | 2 |
| **ADC** | 4× 12-bit |
| **PWM** | 16 channels |
| **Other** | On-chip clock/timer, temp sensor, floating-point library, 12× PIO state machines |

## Getting Started

### MicroPython

1. Install [Thonny IDE](https://thonny.org)
2. Connect the board to your PC via USB
3. In Thonny: configure interpreter to **MicroPython (Raspberry Pi Pico)**
4. Download the MicroPython firmware (.uf2)
5. Hold **BOOTSEL**, connect USB → an **RPI-RP2** drive appears
6. Drag the .uf2 file onto the drive — the board reboots automatically
7. Start coding in Thonny's editor

### C/C++ (VSCode Extension)

1. Install **VSCode** and the **Raspberry Pi Pico** extension (from .vsix)
2. Configure paths: CMake, Git, Ninja, Python3
3. Create a new project, select SDK version
4. Choose toolchain: **13.2.Rel1** (ARM) or **RISCV.13.3** (RISC-V)
5. Select the board, click **Compile** → produces a .uf2 file
6. Flash via the extension's **Run** button or by drag-and-drop the .uf2

### Arduino IDE

1. Install [Arduino IDE](https://www.arduino.cc/en/software)
2. Add board URL in **File → Preferences**:
   ```
   https://github.com/earlephilhower/arduino-pico/releases/download/4.5.2/package_rp2040_index.json
   ```
3. Install **Raspberry Pi Pico/RP2040** boards in Board Manager
4. Hold **BOOTSEL** + connect USB, select the **uf2 Board** port
5. Choose the correct board model and upload

## Sample Experiments

- External LED
- Traffic Light System
- Burglar Alarm (LED + Buzzer)
- Potentiometer (ADC)
- WS2812 RGB LED
- LCD1602 I2C Display

## Resources

- [Raspberry Pi Pico SDK](https://github.com/raspberrypi/pico-sdk)
- [MicroPython firmware for Pico 2](https://micropython.org/download/RPI_PICO2/)
- [Arduino-Pico Core](https://github.com/earlephilhower/arduino-pico)
- [Raspberry Pi Pico VS Code Extension](https://www.raspberrypi.com/news/pico-vscode-extension/)
