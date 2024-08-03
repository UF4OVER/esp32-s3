import time

from machine import DAC, Pin

dac_pin = Pin(26, Pin.OUT)
dac = DAC(dac_pin)
while True:
    # 呼吸效果
    for i in range(0, 1023):
        dac.write(i)
        time.sleep_ms(10)
    for i in range(1023, 0, -1):
        dac.write(i)
        time.sleep_ms(10)
