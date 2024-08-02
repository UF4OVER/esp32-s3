import machine

import UTB

adc1 = machine.ADC(machine.Pin(13))
adc1.atten(machine.ADC.ATTN_11DB)

adc2 = machine.ADC(machine.Pin(14))
adc2.atten(machine.ADC.ATTN_11DB)

uart1 = machine.UART(1, tx=1, rx=2, baudrate=115200)
s1 = UTB.UBT_SERVO(uart1,1)
s8 = UTB.UBT_SERVO(uart1,8)




    
    s1.servo_do(int((ave1/78)-48),0,0,0)
    s8.servo_do(int((ave2/78)-48),0,0,0)    



    
