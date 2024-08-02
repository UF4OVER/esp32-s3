import machine
import neopixel

rgb = neopixel.NeoPixel(machine.Pin(48), 4)
rgb.fill((250, 0, 0))

rgb.write()
