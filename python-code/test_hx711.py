from machine import Pin, Timer
import time

class HX711:
    def __init__(self, dout, sck):
        self.dout = Pin(dout, Pin.IN)
        self.sck = Pin(sck, Pin.OUT, value=0)

    def read(self):
        # Wait for DOUT to go low (data ready)
        timeout = 1000
        while self.dout.value() and timeout:
            timeout -= 1
            time.sleep_us(1)

        if timeout == 0:
            return None  # timeout

        value = 0
        for _ in range(24):
            self.sck.on()
            time.sleep_us(1)
            value = (value << 1) | self.dout.value()
            self.sck.off()
            time.sleep_us(1)

        # 25th pulse to set gain=128
        self.sck.on()
        time.sleep_us(1)
        self.sck.off()

        # Convert to signed
        if value & 0x800000:
            value |= ~0xFFFFFF
        return value

# Pins: GP26 = DOUT (DT), GP27 = SCK
hx = HX711(dout=26, sck=27)

print("HX711 Weight Sensor Test")
print("Reading raw values...")
print("(Place an object on the sensor and watch the numbers change)")
print()

# Read a few values to stabilize
for _ in range(5):
    hx.read()
    time.sleep_ms(100)

while True:
    val = hx.read()
    if val is not None:
        print("Raw:", val)
    else:
        print("No sensor detected!")
    time.sleep_ms(500)
