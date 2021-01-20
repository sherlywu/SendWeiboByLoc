import csv
import re
import time
import os

data = []
def read_csv():
    with open('data.csv', mode='r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)
        column = [row for row in reader]
        # global data
        for message in column:
            tmp = []
            tmp.append(message[0])
            tmp.append(message[2])
            # print('tmp',type(tmp))
            message1 = str(message)
            ls = re.findall("\d+", message1)
            # print(ls)
            if ls != []:
                startx = int(ls[0])
                starty = int(ls[1])
                endx = int(ls[2])
                endy = int(ls[3])
                x = (endx - startx) / 2 + startx
                y = (endy - starty) / 2 + starty
                message2 = ((x, y))
                # print(message2)
                tmp.append(message2)
                tmp.pop(1)
            data.append(tuple(tmp))
        print(data)
        return data


def send_weibo():
        for loc in data:
            # print(loc[1])
            click_event = 'adb shell input tap '
            input_event = 'adb shell input text '
            if loc[0] == 'click':
                # 字符串拼接 执行点击命令
                os.system(f'{click_event} {loc[1][0]} {loc[1][1]}')
                time.sleep(1)
            if loc[0] == 'type':
                os.system(f'{input_event} {loc[1]}')

read_csv()
send_weibo()
