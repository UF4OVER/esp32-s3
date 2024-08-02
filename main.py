import time

import machine

a = machine.Pin(2)
a.value(1)
time.sleep(1)
a.value(0)
