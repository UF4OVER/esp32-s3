import time

import machine

a = machine.Pin(2)
while 1:

    a.on
    print("on")
    time.sleep(1)
    a.off
