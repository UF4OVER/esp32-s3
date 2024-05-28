import time
from ST7735 import TFT
from sysfont import sysfont
from machine import SPI, Pin, ADC
import math


j1 = Pin(2, Pin.OUT)
j2 = Pin(3, Pin.OUT)
j3 = Pin(4, Pin.OUT)


spi = SPI(2, baudrate=2000000, polarity=0, phase=0, sck=Pin(16), mosi=Pin(15))
tft = TFT(spi, 41, 42, 45)
tft.initr()
tft.rgb(True)

def jietibo():
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
    
def testfastlines(color1, color2):
    # 网格-griding
    tft.fill(TFT.BLACK)
    for y in range(0, tft.size()[1], 5):
        tft.hline((0, y), tft.size()[0], color1)

    for x in range(0, tft.size()[0], 5):
        tft.vline((x, 0), tft.size()[1], color2)
testfastlines(0x66, 0x55)
tft.line((0,120),(120,120),TFT.WHITE)
tft.line((10,128),(10,25),TFT.WHITE)
  

def draw():
    time.sleep(2)
    tft.line((10,120),(25,90),TFT.WHITE)
    tft.line((10,120),(25,70),TFT.WHITE)
    tft.line((10,120),(25,60),TFT.WHITE)

    tft.line((25,90),(40,80),TFT.WHITE)
    tft.line((25,70),(40,60),TFT.WHITE)
    tft.line((25,60),(40,50),TFT.WHITE)

    tft.line((40,80),(70,70),TFT.WHITE)
    tft.line((40,60),(70,50),TFT.WHITE)
    tft.line((40,50),(70,40),TFT.WHITE)
    
    tft.line((70,70),(90,65),TFT.WHITE)
    tft.line((70,50),(90,45),TFT.WHITE)
    tft.line((70,40),(90,35),TFT.WHITE) 
  
# 初始化ADC引脚来读取集电极电压  
adc = ADC(Pin(1))  
adc.atten(ADC.ATTN_11DB)  
adc.width(ADC.WIDTH_12BIT)  
  
# 初始化GPIO引脚来控制基极  
base_pin = Pin(2, Pin.OUT)  
emitter_resistor = 1000  # 假设发射极电阻为1kΩ  
collector_resistor = 10000  # 假设集电极电阻为10kΩ  
supply_voltage = 3.3  # 电源电压，假设为3.3V  
  
# 设置基极电压为高电平和低电平来测试三极管  
def test_transistor_type():  
    base_pin.off()  # 将基极设置为低电平  
    time.sleep(0.1)  # 等待稳定  
    collector_voltage_low = adc.read_u16() * supply_voltage / 65536  
      
    base_pin.on()  # 将基极设置为高电平（ESP32的GPIO默认高电平为3.3V）  
    time.sleep(0.1)  # 等待稳定  
    collector_voltage_high = adc.read_u16() * supply_voltage / 65536  
      
    # 分析电压变化  
    if collector_voltage_low > collector_voltage_high:  
        print("The transistor is likely an NPN type.")
        tft.text((3, 15), "please wait!", TFT.RED, sysfont, 1, nowrap=True)
        tft.text((3, 3), "type:NPN", TFT.RED, sysfont, 1, nowrap=True)
        draw()
        
        
    elif collector_voltage_low < collector_voltage_high:  
        print("The transistor is likely a PNP type.")
        tft.text((3, 3), "type:PNP", TFT.RED, sysfont, 1, nowrap=True)
        tft.text((3, 10), "no pic", TFT.RED, sysfont, 1, nowrap=True)
    
        
    else:  
        print("Unable to determine transistor type or the transistor is not working as expected.")  
        tft.text((3, 3), "Uncommuiate", TFT.RED, sysfont, 1, nowrap=True)
# 执行测试  
test_transistor_type()





    



















