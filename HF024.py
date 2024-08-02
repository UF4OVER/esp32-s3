import time

from machine import UART



class HF024(object):
    """
HF024的micropython驱动
    """

    def __init__(self, uart):  
        self.UART = uart  
        self.UART.write("RESET();\r\n") # 上电复位
        time.sleep(0.5)
        self.UART.write("JUMP(0);\r\n")  # 默认跳转至首页，使用 \r\n 作为换行符
        print("version :",self.UART.write(f'VER;\r\n')) #打印版本信息

    def res(self):
        """
        复位
        """
        self.UART.write(f'RESET();\r\n')
        
    def jump(self,page):
        """
        跳转图页
        """
        self.UART.write(f'JUMP({page});\r\n')
        print(f"jump({page})")
        
    def light(self, light: int):  
        """  
        屏幕亮度调整  
        :param light: 亮度选择，0-255  
        """  
        BL = f'BL({light});\r\n'  
        self.UART.write(BL)  
        print(f"bl({light})")

    def prog(self, channel: int, bar: int):
        """
        进度条
        :param channel: 通道选择
        :param bar :进度选择（0-100）
        """
        SET_PROG = f'SET_PROG({channel},{bar});\r\n'
        self.UART.write(SET_PROG)

    def LCD(self, switch=1):
        """
        背光选择，默认为开启
        :param switch: 1开启背光，0关闭背光
        :return: 单线发送
        """
        LCD_1 = f'LCD({switch});/r/n'
        UART.write(LCD_1)

    def qbar(self, channel: int, web: str):
        """
        二维码的更新
        :param channel: 通道选择
        :param web: 网址
        :return:单项发送，覆盖内容
        """
        QBAR = f'QBAR({channel},{web});/r/n'
        UART.write(QBAR)

    def point(self, channel, angle：int):
        """
        指针的角度
        :param channel 通道选择
        :param angle: 旋转角度0-360
        :return:
        """
        SET_POINT = f'SET_POINT({channel},{angle});/r/n'
        UART.write(SET_POINT)

    def txt(self, channel: int, text: str):
        """

        :param channel 
        :param text 替换的文本，最多支持16个字符，建议原先几个，之后就几个
        """
        text_1 = f'SET_TXT({channel},{text});/r/n'
        UART.write(text_1)

