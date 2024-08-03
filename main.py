import time

import machine
import neopixel

rgb = neopixel.NeoPixel(machine.Pin(48), 1)

while True:
    # 渐变多层次呼吸灯
    for i in range(0, 255):
        rgb.fill((i, 0, 0))
        rgb.write()
        time.sleep(0.01)

    for i in range(0, 255):
        rgb.fill((0, i, 0))
        rgb.write()
        time.sleep(0.01)

    for i in range(0, 255):
        rgb.fill((0, 0, i))
        rgb.write()
        time.sleep(0.01)

    for i in range(0, 255):
        rgb.fill((255 - i, 0, 0))
        rgb.write()
        time.sleep(0.01)

    for i in range(0, 255):
        rgb.fill((0, 255 - i, 0))
        rgb.write()
        time.sleep(0.01)

    for i in range(0, 255):
        rgb.fill((0, 0, 255 - i))
        rgb.write()
        time.sleep(0.01)

    for i in range(0, 255):
        rgb.fill((255 - i, 255 - i, 0))
        rgb.write()
        time.sleep(0.01)


    for i in range(0, 255):
        rgb.fill((255 - i, 0, 255 - i))
        rgb.write()
        time.sleep(0.01)

    for i in range(0, 255):
        rgb.fill((0, 255 - i, 255 - i))
        rgb.write()
        time.sleep(0.01)

    for i in range(0, 255):
        rgb.fill((255 - i, 255 - i, 255 - i))
        rgb.write()
        time.sleep(0.01)
