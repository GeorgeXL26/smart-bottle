from machine import Pin, ADC, I2C
import ssd1306
import time

# === OLED (GP0=SDA, GP1=SCL) ===
print("Testing OLED...")
try:
    i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
    devices = i2c.scan()
    if 0x3C in devices:
        oled = ssd1306.SSD1306_I2C(128, 64, i2c)
        oled.fill(0)
        oled.text("All working!", 0, 0)
        oled.text("OLED - OK", 0, 15)
        oled.text("FSR -", 0, 30)
        oled.text("LED -", 0, 45)
        oled.show()
        print("  OLED OK - found at 0x3C")
    else:
        print("  OLED not found!")
except Exception as e:
    print("  OLED error:", e)

# === FSR402 Pressure Sensor (GP27) ===
fsr = ADC(Pin(27))

# === Pico LED (GP25) ===
led = Pin(25, Pin.OUT)

print("Reading FSR402 and blinking LED...")
print("(Press the FSR402 pad with your finger)")

for i in range(20):
    val = fsr.read_u16()

    # LED on if FSR pressed
    if val > 30000:
        led.on()
    else:
        led.off()

    # Update OLED
    try:
        oled.fill(0)
        oled.text("All working!", 0, 0)
        oled.text("OLED - OK", 0, 15)
        oled.text("FSR - " + str(val), 0, 30)
        oled.text("LED - " + ("ON" if val > 30000 else "OFF"), 0, 45)
        oled.text("Press sensor!", 0, 55)
        oled.show()
    except:
        pass

    print("FSR reading:", val)
    time.sleep_ms(300)

# Turn LED off
led.off()
print("Test complete!")
