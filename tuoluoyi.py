import time
from machine import SoftI2C, Pin
from mpu9250 import MPU9250

PIN_CLK = 29   # PB13, get the pin number from get_pin_number.py
PIN_SDA = 30   # PB14

  # Select the PIN_CLK as the clock
  # Select the PIN_SDA as the data line

i2c = SoftI2C(scl = Pin(14), sda = Pin(13), freq = 100000)
sensor = MPU9250(i2c)

print("MPU9250 id: " + hex(sensor.whoami))

while True:
    print(sensor.acceleration)
    #print(sensor.gyro)
    time.sleep_ms(10)
