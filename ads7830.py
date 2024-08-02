from machine import I2C, Pin

# 命令字节定义
_ADS7828_CMD_SD_SE = 0x80  # 单端输入
_ADS7828_CMD_PD1 = 0x04  # 内部参考电压关闭，AD转换器打开
_ADS7828_CMD_PD3 = 0x0C  # 内部参考电压打开，AD转换器打开

# 使用内部参考电压
_INTERNAL_REF = _ADS7828_CMD_PD3

# 使用外部参考电压
_EXTERNAL_REF = _ADS7828_CMD_PD1

# 创建I2C对象
i2c = I2C(scl=Pin(22), sda=Pin(21))


class ads7830():
    def __init__(self, i2c, address=0x48):
        self.i2c = i2c
        self.address = address

    def read_channel(self, channel, use_internal_ref=True):
        """
        读取ADS7828/ADS7830的指定通道电压。
        :param channel: 通道号（0-7）
        :param use_internal_ref: 是否使用内部参考电压
        :return: 电压值
        """
        # 构建命令字节
        cmd = _ADS7828_CMD_SD_SE | _INTERNAL_REF if use_internal_ref else _EXTERNAL_REF
        cmd |= ((channel >> 1) | (channel & 0x01) << 2) << 4

        # 发送命令并读取结果
        self.i2c.writeto(self.address, bytes([cmd]))
        result = self.ic2.readfrom(self.address, 2)

        # 解析结果
        adc_value = (result[0] << 8) | result[1]

        # 返回电压值，这里简化处理，未考虑分辨率和参考电压
        return adc_value


# 示例：读取通道0电压
ads7830 = ads7830(i2c)
voltage = ads7830.read_channel(0)
print(f"Channel 0 voltage: {voltage}")
