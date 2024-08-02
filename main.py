import time

import machine

led = machine.Pin(2, machine.Pin.OUT)
while 1:
    led.on()
    print("LED is on.")
    time.sleep(1)
    led.off()
    print("LED is off.")
    time.sleep(1)
