ADC_VIN_H_REGISTER = 0x30
ADC_VOUT_H_REGISTER = 0x31
ADC_VIN_VOUT_L_REGISTER = 0x32
ADC_IVIN_H_REGISTER = 0x33
ADC_IVOUT_H_REGISTER = 0x34
ADC_IVIN_VOUT_L_REGISTER = 0x35


class sw35xx:
    def __init__(self, i2c, DEVICE_ADDRESS):
        self.i2c = i2c
        self.DEVICE_ADDRESS = DEVICE_ADDRESS
        self.i2c.writeto_mem(DEVICE_ADDRESS, 0x13, 2)
        self.version = hex(i2c.readfrom_mem(60, 1, 1)[0])
        self.data = i2c.readfrom_mem(60, 7, 1)
        self.data1 = i2c.readfrom_mem(60, 6, 1)
        self.pwr_status = self.data[0]

    def usb_switch(self):
        _ctrl_buck_on = (self.pwr_status >> 2) & 0x01
        _ctrl_2port_on = (self.pwr_status >> 1) & 0x01
        _ctrl_1port_on = self.pwr_status & 0x01
        return _ctrl_buck_on, _ctrl_2port_on, _ctrl_1port_on

    def set_adc_vin_enable(self, enable):
        self.i2c.writeto_mem(self.DEVICE_ADDRESS, 0xd, bytearray([enable]))

    def get_v(self):
        vin_high_bytes = self.i2c.readfrom_mem(self.DEVICE_ADDRESS, ADC_VIN_H_REGISTER, 1)
        vin_high = vin_high_bytes[0]

        vout_high_bytes = self.i2c.readfrom_mem(self.DEVICE_ADDRESS, ADC_VOUT_H_REGISTER, 1)
        vout_high = vout_high_bytes[0]

        vin_vout_low_bytes = self.i2c.readfrom_mem(self.DEVICE_ADDRESS, ADC_VIN_VOUT_L_REGISTER, 1)
        vin_vout_low = vin_vout_low_bytes[0]

        vin_data = ((vin_high << 4) | (vin_vout_low >> 4)) * 10

        vout_data = ((vout_high << 4) | (vin_vout_low & 0x0F)) * 6

        return vin_data, vout_data

    def get_iout(self):
        Ivin_high_bytes = self.i2c.readfrom_mem(self.DEVICE_ADDRESS, ADC_IVIN_H_REGISTER, 1)
        Ivin_high = Ivin_high_bytes[0]

        Ivout_high_bytes = self.i2c.readfrom_mem(self.DEVICE_ADDRESS, ADC_IVOUT_H_REGISTER, 1)
        Ivout_high = Ivout_high_bytes[0]

        Ivin_vout_low_bytes = self.i2c.readfrom_mem(self.DEVICE_ADDRESS, ADC_IVIN_VOUT_L_REGISTER, 1)
        Ivin_vout_low = Ivin_vout_low_bytes[0]

        usb1 = ((Ivin_high << 4) | (Ivin_vout_low >> 4)) * 2.5

        usb2 = ((Ivout_high << 4) | (Ivin_vout_low & 0x0F)) * 2.5

        return usb1, usb2

    def protocol(self):
        if self.data1:

            fcx_status = self.data1[0]

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
            elif fcx_ind == 1:
                print("快充协议指示: QC2.0")
            elif fcx_ind == 2:
                print("快充协议指示: QC3.0")
            elif fcx_ind == 3:
                print("快充协议指示: FCP")
            elif fcx_ind == 4:
                print("快充协议指示: SCP")
            elif fcx_ind == 5:
                print("快充协议指示: PD FIX")
            elif fcx_ind == 6:
                print("快充协议指示: PD PPS")
            elif fcx_ind == 7:
                print("快充协议指示: PE1.1")
            elif fcx_ind == 8:
                print("快充协议指示: PE2.0")
            elif fcx_ind == 9:
                print("快充协议指示: VOOC")
            elif fcx_ind == 10:
                print("快充协议指示: SFCP")
            else:
                print("快充协议指示: Reserved or Unknown")
        else:
            print("无法从I2C设备读取数据")
