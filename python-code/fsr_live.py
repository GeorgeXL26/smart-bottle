from machine import Pin, ADC, I2C
import ssd1306
import time

# OLED (GP0=SDA, GP1=SCL)
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# FSR402 pressure sensor (GP27)
fsr = ADC(Pin(27))
pico_led = Pin(25, Pin.OUT)

# Read initial "no press" baseline
baseline = fsr.read_u16()
print("Baseline (no press):", baseline)

while True:
    raw = fsr.read_u16()
    diff = abs(raw - baseline)
    pressed = diff > 3000

    if pressed:
        pico_led.on()
    else:
        pico_led.off()

    # Show on OLED
    oled.fill(0)
    oled.text("Smart Bottle", 15, 0)
    oled.text("============", 5, 12)
    oled.text("Reading: " + str(raw), 10, 28)

    if pressed:
        oled.text("PRESSED!", 40, 45)
    else:
        oled.text("No press", 40, 45)

    oled.show()
    time.sleep_ms(500)
