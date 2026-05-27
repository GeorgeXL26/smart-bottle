from machine import Pin
import time

led = Pin(25, Pin.OUT)
print("LED test started — blinks 5 times")

for i in range(5):
    led.on()
    print(f"LED ON ({i+1}/5)")
    time.sleep(1)
    led.off()
    print(f"LED OFF ({i+1}/5)")
    time.sleep(1)

print("LED test complete!")
