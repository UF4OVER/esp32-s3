import time

import machine
import time

import machine

j1 = machine.Pin(2, machine.Pin.OUT)
j2 = machine.Pin(3, machine.Pin.OUT)
j3 = machine.Pin(4, machine.Pin.OUT)


while 1:
    
    j1.value(0)
    j2.value(0)
    j3.value(0)
    time.sleep_ms(20)
    j1.value(0)
    j2.value(0)
    j3.value(1)
    time.sleep_ms(20)
    j1.value(0)
    j2.value(1)
    j3.value(0)
    time.sleep_ms(20)
    j1.value(0)
    j2.value(1)
    j3.value(1)
    time.sleep_ms(20)
    j1.value(1)
    j2.value(0)
    j3.value(0)
    time.sleep_ms(20)
    j1.value(1)
    j2.value(0)
    j3.value(1)
    time.sleep_ms(20)
    j1.value(1)
    j2.value(1)
    j3.value(0)
    time.sleep_ms(20)
    j1.value(1)
    j2.value(1)
    j3.value(1)
    time.sleep_ms(20)
    