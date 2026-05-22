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

If you haven't drunk water in **1 hour**, a reminder message appears on the screen.

## Features

- **Weight sensor** — detects when you drink
- **OLED display** — shows the penguin pet at each stage
- **Screen reminder** — displays "Remember to drink more water!" when idle
- **Auto-reset** — penguin resets to egg every morning

## Hardware Requirements

| Component | Purpose | Est. Cost (SGD) |
|-----------|---------|----------------|
| Raspberry Pi Pico 2 | Microcontroller (brain) | $8–10 |
| 0.96" OLED (I2C) | Display | $9–12 |
| 1kg Load Cell + HX711 | Weight sensor | $10–14 |
| 3.7V LiPo Battery (1000mAh) | Power | $8–12 |
| TP4056 Charging Module | Battery charging | $2–3 |
| Breadboard + Jumper Wires | Connections | $5–8 |
| **Total** | | **~$37–57** |

## Logic Flow

1. **Morning** — Bottle powers on → Screen shows Blue Egg
2. **Noon** — No water for 1 hour → Screen reminder appears
3. **Afternoon** — Drinks half → Screen shows Penguin Chick
4. **Evening** — Bottle empty → Screen shows Big Blue Penguin
5. **Next day** — Refill and restart → Resets to Blue Egg

## Why Raspberry Pi Pico 2?

- **Cost**: ~$7.50 SGD vs $65–205 for a Raspberry Pi 5
- **Battery life**: Runs days/weeks on small battery vs hours on Pi 5
- **Startup**: Instant (<1s) vs 20–40s boot time on Pi 5
- **Size & heat**: Compact and cool vs heavy and hot

## Project Structure

```
gep-ivp-project/
├── README.md          # This file
└── Smart bottle.md    # Full project plan & hardware procurement list
```
