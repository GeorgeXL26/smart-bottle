# Penguin Smart Bottle 🐧

An IoT smart water bottle designed for students who forget to drink water. It features a **virtual penguin pet** that grows as you stay hydrated — turning hydration into a game.

**Target audience**: Students who do not drink water often.

## How It Works

The bottle tracks water intake using a weight sensor. The more you drink, the more your penguin pet grows:

| Stage | State | Screen |
|-------|-------|--------|
| 🥚 | Morning / Reset | Blue Egg |
| 🐤 | Drank some water | Penguin Chick |
| 🐧 | Bottle emptied | Big Blue Penguin |

If you haven't drunk water in **1 hour**, the bottle vibrates and reminds you. At night, flip the sleep switch to silence everything.

## Features

- **Weight sensor** — detects when you drink
- **OLED display** — shows the penguin pet at each stage
- **Vibration motor** — gentle nudge reminders
- **Voice reminder** — speaker says "Remember to drink more water!"
- **Exam mode** — silent mode; shows reminder text on screen instead
- **Sleep mode** — cuts power to the motor for quiet nights
- **Auto-reset** — penguin resets to egg every morning

## Hardware Requirements

| Component | Purpose | Est. Cost (SGD) |
|-----------|---------|----------------|
| Raspberry Pi Pico 2 | Microcontroller (brain) | $8–10 |
| 0.96" OLED (I2C) | Display | $9–12 |
| 1kg Load Cell + HX711 | Weight sensor | $10–14 |
| 3.7V LiPo Battery (1000mAh) | Power | $8–12 |
| TP4056 Charging Module | Battery charging | $2–3 |
| Mini Vibration Motor | Nudge reminder | — |
| Speaker | Voice reminder | — |
| Toggle switches | Sleep/Exam mode | — |
| Breadboard + Jumper Wires | Connections | $5–8 |
| **Total** | | **~$46–69** |

## Logic Flow

1. **Morning** — Flip switch ON → Screen shows Blue Egg
2. **Noon** — No water for 1 hour → Bottle vibrates
3. **Afternoon** — Drinks half → Screen shows Penguin Chick
4. **Evening** — Bottle empty → Screen shows Big Blue Penguin
5. **Night** — Flip switch OFF → Sleeping Penguin
6. **Next day** — Flip ON → Resets to Blue Egg

## Why Raspberry Pi Pico 2?

- **Cost**: ~$7.50 SGD vs $65–205 for a Raspberry Pi 5
- **Battery life**: Runs days/weeks on small battery vs hours on Pi 5
- **Startup**: Instant (<1s) vs 20–40s boot time on Pi 5
- **Size & heat**: Compact and cool vs heavy and hot

## Project Structure

```
gep-ivp-project/
├── README.md                # This file
├── Smart bottle.md          # Full project plan & hardware procurement list
└── tech-support/
    └── github-setup-guide.md  # GitHub setup & workflow guide for juniors
```

---

## Authors

- **Xinli**
- **Yuxuan**
