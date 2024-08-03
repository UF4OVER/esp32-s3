import machine
import neopixel

rgb = neopixel.NeoPixel(machine.Pin(48), 1)
rgb.fill((255, 0, 0))
rgb.write()
