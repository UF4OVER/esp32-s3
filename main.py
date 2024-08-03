import machine
import neopixel

rgb = neopixel.NeoPixel(machine.Pin(48), 1)
# 渐变呼吸灯
while True:
    for i in range(0, 255):
        rgb.fill((i, 255 - i, 0))
        rgb.write()
    for i in range(0, 255):
        rgb.fill((255 - i, 0, i))
        rgb.write()
    # for i in range(0, 255):
    #     rgb.fill((0, i, 255 - i))
    #     rgb.write()
