# FSR402 Pressure Sensor Test

## Wiring

| FSR402 | → | Pico 2 |
|--------|---|--------|
| Pin 1 | → | **GP27** / ADC1 (pin 32) |
| Pin 2 | → | **GND** (pin 38) |
| VCC (optional) | → | **3V3** via 10kΩ pull-down resistor for stable readings |

## Code

File: `python-code/fsr_live.py`

The code reads the FSR402 pressure sensor via ADC on GP27 and displays the raw value on the OLED (I2C on GP0/GP1). The Pico's onboard LED lights up when pressure is detected.

## How to Run

```bash
mpremote run python-code/fsr_live.py
```

The OLED displays:
- **Reading:** current raw ADC value (0-65535)
- **PRESSED!** / No press — status text

Press the black round pad of the FSR402 with your finger to see the value change.

## Notes

- The FSR402 is a **pressure sensor**, not a weight sensor. It detects force applied to the pad.
- For precise weight measurement, use a **load cell + HX711 module** instead.
- Raw ADC values vary depending on wiring (pull-up/pull-down resistors).
