import gc

import machine
import network
import urequests as requests


def connect_wlan(ssid, password):
    sta_if = network.WLAN(network.STA_IF)
    ap_if = network.WLAN(network.AP_IF)
    sta_if.active(True)
    ap_if.active(False)

    if not sta_if.isconnected():
        print("Connecting to WLAN ({})...".format(ssid))
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            print("Connecting...")
            pass

    print("Connected to {}.".format(ssid))
    return True


SSID = "test_div"
PASSWORD = "00000000"

gc.collect()

try:
    connect_wlan(SSID, PASSWORD)
except Exception as e:
    print("WLAN connection failed:", e)
t
gc.collect()

url = 'https://gitee.com/uf4/esp32-s33/raw/master/main.py'
response = requests.get(url)
print("ok")

chunk_size = 100  #

with open("main.py", "w") as f:
    content = response.content
    position = 0

    while position < len(content):
        chunk = content[position:position + chunk_size]
        f.write(chunk.decode())  # 写文件
        position += chunk_size
        gc.collect()  # 回收内存

print("main.py updated successfully.")
machine.reset()
