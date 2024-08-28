import gc

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
    # 在这里可以添加额外的处理逻辑，如重试或通知用户
    raise  # 抛出异常以终止程序执行
gc.collect()

url = 'https://gitee.com/uf4/esp32-s33/raw/master/main.py'

# Get the remote file's content
remote_response = requests.get(url)

print("Updating main.py...")
chunk_size = 100


with open("main.py", "w") as f:
    content = remote_response.content
    position = 0

    while position < len(content):
        chunk = content[position:position + chunk_size]
        f.write(chunk.decode())  # Write each chunk to the file
        position += chunk_size
        gc.collect()

print("main.py updated successfully.")
exec(open("main.py").read())
