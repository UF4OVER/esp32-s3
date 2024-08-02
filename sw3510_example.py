import time

from machine import Pin, SoftI2C

import sw35xx

# spi = SPI(2, baudrate=20000000, polarity=0, phase=0, sck=Pin(13), mosi=Pin(14))
#
# tft=TFT(spi,10,11,12)
# tft.initr()
# tft.rgb(True)
# tft.fill(TFT.BLACK)

i2c = SoftI2C(scl=Pin(18), sda=Pin(17), freq=9600)

print(i2c.scan())

DEVICE_ADDRESS = 60

sw = sw35xx.sw35xx(i2c, DEVICE_ADDRESS)
usb1, usb2 = sw.get_v()
i1, i2 = sw.get_iout()
while 1:
    i1, i2 = sw.get_iout()
    print(i1 / 1000)

    time.sleep(0.1)
