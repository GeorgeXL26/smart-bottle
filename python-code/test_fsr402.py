from machine import Pin, ADC
import time

# FSR402 pressure sensor on GP27 (ADC1)
fsr = ADC(Pin(27))

print("FSR402 Pressure Sensor Test")
print("Press the sensor to see the value change")
print()

while True:
    # Read 16-bit ADC value (0-65535)
    val = fsr.read_u16()
    print("FSR402 Raw:", val)
    time.sleep_ms(300)
