# Smart Bottle — Design & User Flow

## Hardware Setup

### Components

| Component | Pins | Notes |
|-----------|------|-------|
| Pico 2 | — | MicroPython |
| OLED (color upgrade) | TBD | ST7789 or similar |
| HX711 weight sensor | GP26 (DT), GP27 (SCK) | Read bottle weight |
| Button A — Confirm | GP2 | Full/empty calibration, confirm |
| Button B — Mode | GP3 | Toggle display mode / cycle screens |
| Button C — Tare | GP4 | Recalibrate for new bottle |

## Button Functions

| Button | Setup Mode | Normal Mode |
|--------|------------|-------------|
| **Confirm** (GP2) | Record weight, confirm choice | Wake display |
| **Mode** (GP3) | Toggle Numbers ↔ Penguin | Cycle screens |
| **Tare** (GP4) | Skip / go back | Zero sensor for new bottle |

## Initial Setup Flow

```
Power ON
  │
  ├── First time or bottle changed?
  │      │
  │      ├── Yes → SETUP MODE
  │      │         │
  │      │         1. "Place FULL bottle, press Confirm"
  │      │            → Records full_bottle_weight
  │      │
  │      │         2. "Place EMPTY bottle, press Confirm"
  │      │            → Records empty_bottle_weight
  │      │
  │      │         3. "Select display mode:"
  │      │            [67 Cycle]  or  [Penguin Cycle]
  │      │            Press Mode to toggle
  │      │            Press Confirm to select
  │      │            → Saves to memory
  │      │
  │      └── No → NORMAL MODE
  │
  └── NORMAL MODE
         │
         ├── Calculate water %
         │    water_pct = (current - empty) / (full - empty) * 100
         │
         ├── If mode = 67 Cycle:
         │    Display water level as 0-7 (e.g. "Water: 4/7")
         │
         ├── If mode = Penguin:
         │    Show penguin stage based on water %
         │    Egg → Chick → Penguin
         │
         └── If idle > 1 hour:
              Show reminder message
```

## Display Modes

### 67 Cycle Mode
Shows water level as a simple number 0-7 (or 0%-100%).

### Penguin Cycle Mode
Shows a virtual penguin that grows as you drink:

| Water % | Stage |
|---------|-------|
| 0% | Egg |
| 1%-49% | Chick (hatching) |
| 50%-99% | Young Penguin |
| 100% | Full-grown Penguin |

## Calibration (Tare)

Pressing **Tare** (GP4) anytime in normal mode restarts the setup flow, allowing the user to recalibrate with a different bottle — no code changes needed.

## Power Management

- OLED turns off after 60s of inactivity ("sleep mode")
- Press any button to wake
- Weight sensor reading stops during sleep to save battery
