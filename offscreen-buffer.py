from machine import SPI, Pin

from ST7735 import TFT


spi = SPI(2, baudrate=20000000, polarity=0, phase=0, sck=Pin(46), mosi=Pin(45), miso=Pin(0))
tft=TFT(spi,43,42,15)
tft.initr()
tft.rgb(True)
tft.fill(TFT.BLACK)

from framebuf import FrameBuffer, RGB565
buf = bytearray(128*160*2)
fb = FrameBuffer(buf, 127, 160, RGB565)

tft._setwindowloc((0,0),(127,159))

size=20
(xmax, ymax) = (128-size, 160-size)
(x, y) = (size, size)
(vx, vy) = (1, 1)

while True:
    fb.fill(0)
    fb.ellipse(x, y, size, size, 0xffff, True)
    x += vx
    if x == xmax or x == size:
        vx = -vx
    y += vy
    if y == ymax or y == size:
        vy = -vy
    tft._writedata(buf)
