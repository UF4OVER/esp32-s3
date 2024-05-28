from ST7735 import TFT
from sysfont import sysfont
from machine import SPI, Pin, SoftI2C
import time
import math

spi = SPI(2, baudrate=20000000, polarity=0, phase=0, sck=Pin(13), mosi=Pin(14))

tft = TFT(spi, 10, 11, 12)
tft.initr()
tft.rgb(True)
tft.fill(TFT.BLACK)

i2c = SoftI2C(scl=Pin(17), sda=Pin(18), freq=9600)

print(i2c.scan())

data = i2c.readfrom_mem(60, 7, 1)

data1 = i2c.readfrom_mem(60, 6, 1)

pwr_status = data[0]

print("PWR_STATUS:", hex(pwr_status))
tft.text((10, 10), hex(pwr_status), TFT.RED, sysfont, 1, nowrap=True)

ctrl_buck_on = (pwr_status >> 2) & 0x01
ctrl_2port_on = (pwr_status >> 1) & 0x01
ctrl_1port_on = pwr_status & 0x01

print("ctrl_buck_on:", ctrl_buck_on)
print("ctrl_2port_on:", ctrl_2port_on)
print("ctrl_1port_on:", ctrl_1port_on)

tft.text((10, 20), "ctrl_buck_on:", TFT.RED, sysfont, 1, nowrap=True)
tft.text((100, 20), f"{ctrl_buck_on}", TFT.RED, sysfont, 1, nowrap=True)
tft.text((10, 30), "ctrl_2port_on: ", TFT.RED, sysfont, 1, nowrap=True)
tft.text((100, 30), f"{ctrl_2port_on} ", TFT.RED, sysfont, 1, nowrap=True)
tft.text((10, 40), "ctrl_1port_on: ", TFT.RED, sysfont, 1, nowrap=True)
tft.text((100, 40), f"{ctrl_1port_on} ", TFT.RED, sysfont, 1, nowrap=True)

DEVICE_ADDRESS = 60


def set_adc_vin_enable(enable):
    i2c.writeto_mem(DEVICE_ADDRESS, 13, bytearray([enable]))


def read_adc_vin_h():
    vin_h_reg = i2c.readfrom_mem(DEVICE_ADDRESS, 30, 1)[0]
    return vin_h_reg


def read_adc_vout_h():
    vout_h_reg = i2c.readfrom_mem(DEVICE_ADDRESS, 31, 1)[0]
    return vout_h_reg


def read_adc_vin_vout_l():
    vin_vout_l_reg = i2c.readfrom_mem(DEVICE_ADDRESS, 32, 1)[0]

    vin_low = (vin_vout_l_reg >> 4) & 0x0F
    vout_low = vin_vout_l_reg & 0x0F
    return vin_low, vout_low


set_adc_vin_enable(1)
vin_high = read_adc_vin_h()
vout_high = read_adc_vout_h()

vin_low, vout_low = read_adc_vin_vout_l()
vin_full = (vin_high << 4) | vin_low
vout_full = (vout_high << 4) | vout_low

print("ADC Vin High 8 bits:", hex(vin_high))
print("ADC Vout High 8 bits:", hex(vout_high))

vin_voltage = vin_full * 10  # 单位：mV，因为10mV/step
vout_voltage = vout_full * 6  # 单位：mV，因为6mV/step  

print("Vin Voltage:", vin_voltage, "mV")
print("Vout Voltage:", vout_voltage, "mV")

if data1:

    fcx_status = data1[0]

    pd_src_spec_ver = (fcx_status >> 4) & 0x03
    if pd_src_spec_ver == 0:
        print("PD协议版本: Reserved")
    elif pd_src_spec_ver == 1:
        print("PD协议版本: PD 2.0")
    elif pd_src_spec_ver == 2:
        print("PD协议版本: PD 3.0")
    else:
        print("PD协议版本: Reserved")

    fcx_ind = fcx_status & 0x0F
    if fcx_ind == 0:
        print("快充协议指示: Reserved")
        tft.text((10, 80), "Reserved", TFT.RED, sysfont, 1, nowrap=True)
    elif fcx_ind == 1:
        print("快充协议指示: QC2.0")
        tft.text((10, 80), "QC2.0:", TFT.RED, sysfont, 1, nowrap=True)
    elif fcx_ind == 2:
        print("快充协议指示: QC3.0")
        tft.text((10, 80), "QC3.0", TFT.RED, sysfont, 1, nowrap=True)
    elif fcx_ind == 3:
        print("快充协议指示: FCP")
        tft.text((10, 80), "FCP:", TFT.RED, sysfont, 1, nowrap=True)
    elif fcx_ind == 4:
        print("快充协议指示: SCP")
        tft.text((10, 80), "SCP:", TFT.RED, sysfont, 1, nowrap=True)
    elif fcx_ind == 5:
        print("快充协议指示: PD FIX")
        tft.text((10, 80), "PD FIX:", TFT.RED, sysfont, 1, nowrap=True)
    elif fcx_ind == 6:
        print("快充协议指示: PD PPS")
        tft.text((10, 80), "PD PPS:", TFT.RED, sysfont, 1, nowrap=True)
    elif fcx_ind == 7:
        print("快充协议指示: PE1.1")
        tft.text((10, 80), "PE1.1:", TFT.RED, sysfont, 1, nowrap=True)
    elif fcx_ind == 8:
        print("快充协议指示: PE2.0")
        tft.text((10, 80), "PE2.0:", TFT.RED, sysfont, 1, nowrap=True)
    elif fcx_ind == 9:
        print("快充协议指示: VOOC")
        tft.text((10, 80), "VOOC:", TFT.RED, sysfont, 1, nowrap=True)
    elif fcx_ind == 10:
        print("快充协议指示: SFCP")
        tft.text((10, 80), "SFCP:", TFT.RED, sysfont, 1, nowrap=True)
    else:
        print("快充协议指示: Reserved or Unknown")
        tft.text((10, 80), "Reserved or Unknown:", TFT.RED, sysfont, 1, nowrap=True)
else:
    print("无法从I2C设备读取数据")
