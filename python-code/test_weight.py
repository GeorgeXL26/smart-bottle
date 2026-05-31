from machine import Pin, ADC, I2C
import ssd1306
import time

# OLED setup (GP0=SDA, GP1=SCL)
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Weight sensor AO connected to GP27 (ADC1)
weight_sensor = ADC(Pin(27))
pico_led = Pin(25, Pin.OUT)

print("Weight sensor test started!")
print("Press the load cell to see changes")

# Calibration: read empty value once
empty_val = weight_sensor.read_u16()

while True:
    raw = weight_sensor.read_u16()       # 0-65535
    diff = raw - empty_val                # change from empty

    # Scale for display (make it readable)
    display_val = abs(diff) // 100

    # Pico LED on if weight detected
    if abs(diff) > 500:
        pico_led.on()
    else:
        pico_led.off()

    # OLED display
    oled.fill(0)
    oled.text("Weight Sensor", 0, 0)
    oled.text("---", 0, 12)
    oled.text("Raw: " + str(raw), 0, 28)
    oled.text("Diff: " + str(display_val), 0, 40)
    oled.text("Press: " + ("YES" if abs(diff) > 500 else "no"), 0, 52)
    oled.show()

    print("Raw:", raw, "| Diff:", display_val)
    time.sleep_ms(200)
