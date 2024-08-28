import time

from machine import Pin

# 行引脚设置为输入
row_pins = [Pin(19, Pin.IN, Pin.PULL_UP),
            Pin(18, Pin.IN, Pin.PULL_UP),
            Pin(5, Pin.IN, Pin.PULL_UP),
            Pin(17, Pin.IN, Pin.PULL_UP)]

# 列引脚设置为输出
col_pins = [Pin(16, Pin.OUT),
            Pin(4, Pin.OUT),
            Pin(2, Pin.OUT),
            Pin(15, Pin.OUT)]


def read_keypad():
    keys = [
        ['1', '2', '3', 'A'],
        ['4', '5', '6', 'B'],
        ['7', '8', '9', 'C'],
        ['*', '0', '#', 'D']
    ]

    for j, col_pin in enumerate(col_pins):
        col_pin.value(0)  # 将当前列设置为低电平
        for i, row_pin in enumerate(row_pins):
            if row_pin.value() == 0:  # 检测行引脚的状态
                # 将当前列恢复为高电平
                col_pin.value(1)
                return keys[i][j]  # 返回按下的按键
        col_pin.value(1)  # 将当前列恢复为高电平

    return None  # 没有按键被按下


# 循环读取键盘状态
while True:
    key = read_keypad()
    if key is not None:
        print("按下的按键:", key)
    time.sleep(0.1)  # 短暂延迟
------
著作权归极客侠
GeeksMan所有
基于GPL
3.0
协议
原文链接：https: // docs.geeksman.com / esp32 / MicroPython / 26.
esp32 - micropython - keyboard.html
