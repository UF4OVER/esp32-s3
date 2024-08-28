import sensor
import time
from pyb import UART

# 初始化传感器
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time=2000)
sensor.set_auto_whitebal(True)
sensor.set_auto_gain(True)

# 初始化串口
uart = UART(3, 115200)

# 阈值定义
red_threshold = [(18, 100, 13, 100, 99, 8), (5, 100, 6, 68, 89, 5), (76, 19, 86, 19, 76, -37)]
green_threshold = [(43, 8, -70, -20, 51, -59), (61, 12, -62, -20, 60, 6), (46, 11, -56, -9, 47, -121)]

# 其他初始化
clock = time.clock()
count = 0
total_x = 0
total_y = 0
total_length = 0
k = 1800
gui = 0
you = 0
target_detected = False


# 获取最大Blob的索引
def get_biggest_blob(blobs):
    max_blob_index = 0
    max_area = 0
    for i, blob in enumerate(blobs):
        area = blob.pixels()
        if area > max_area:
            max_area = area
            max_blob_index = i
    return max_blob_index


# 修改数据格式
def modified_data(data):
    data = int(data)
    str_data = ''
    if data < 10:
        str_data = '000' + str(data)
    elif 10 <= data < 100:
        str_data = '00' + str(data)
    elif 100 <= data < 1000:
        str_data = '0' + str(data)
    else:
        str_data = str(data)
    return str_data.encode('utf-8')


while True:
    clock.tick()
    img = sensor.snapshot()

    if uart.any():
        a = uart.readline().decode().strip()
        print(a)
        b = int(a)

    red_blobs = img.find_blobs(red_threshold)
    green_blobs = img.find_blobs(green_threshold)

    if red_blobs or green_blobs:
        if red_blobs and green_blobs:
            red_index = get_biggest_blob(red_blobs)
            green_index = get_biggest_blob(green_blobs)

            if red_blobs[red_index].pixels() > green_blobs[green_index].pixels():
                target_detected = True
                img.draw_rectangle(red_blobs[red_index].rect())
                img.draw_cross(red_blobs[red_index].cx(), red_blobs[red_index].cy())
                img.draw_rectangle(green_blobs[green_index].rect())

                length = k / ((red_blobs[red_index].w() + red_blobs[red_index].h()) / 2)
                total_x += red_blobs[red_index].cx()
                total_y += red_blobs[red_index].cy()
                total_length += length

                count += 1
                if count == 1:
                    avg_x = total_x / count
                    avg_y = total_y / count
                    avg_length = total_length / count

                    x = modified_data(avg_x)
                    y = modified_data(avg_y)
                    length = modified_data(avg_length)

                    if b == 111:
                        uart.write(modified_data(5))
                        uart.write(x)
                        uart.write(y)
                        uart.write(length)
                        uart.write("\r\n")
                        print("success")

                    total_x = 0
                    total_y = 0
                    count = 0
                    total_length = 0
                    print('type:', 5, 'cx:', x, 'cy:', y, 'length:', length)
                    you = 1
                time.sleep(0.1)

        elif red_blobs:
            index = get_biggest_blob(red_blobs)
            target_detected = True
            img.draw_rectangle(red_blobs[index].rect())
            img.draw_cross(red_blobs[index].cx(), red_blobs[index].cy())

            length = k / ((red_blobs[index].w() + red_blobs[index].h()) / 2)
            total_x += red_blobs[index].cx()
            total_y += red_blobs[index].cy()
            total_length += length

            count += 1
            if count == 1:
                avg_x = total_x / count
                avg_y = total_y / count
                avg_length = total_length / count

                x = modified_data(avg_x)
                y = modified_data(avg_y)
                length = modified_data(avg_length)

                if b == 111:
                    uart.write(modified_data(5))
                    uart.write(x)
                    uart.write(y)
                    uart.write(length)
                    uart.write("\r\n")
                    print("success!!!")

                total_x = 0
                total_y = 0
                count = 0
                total_length = 0
                print('type:', 5, 'cx:', x, 'cy:', y, 'length:', length)
                you = 1
            time.sleep(0.1)

        elif not target_detected and green_blobs:
            index = get_biggest_blob(green_blobs)
            target_detected = True
            img.draw_rectangle(green_blobs[index].rect())

            length = k / ((green_blobs[index].w() + green_blobs[index].h()) / 2)
            total_x += green_blobs[index].cx()
            total_y += green_blobs[index].cy()
            total_length += length

            count += 1
            if count == 1:
                avg_x = total_x / count
