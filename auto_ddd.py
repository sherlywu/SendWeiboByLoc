# log /Users/wuyanjiao/2020/events/event.log
import os
import time

locs = []
with open(r'/Users/wuyanjiao/2020/events/event.log', mode='r', encoding='utf8') as f:
    for line in f.readlines():
        if 'ABS_MT_POSITION_X' in line:
            # 字符串去掉空格后转化为list
            lsx = line.strip().split(' ')
            # 取list中最后一位
            x = lsx[-1]
            # 将16进制转化为10进制
            if int(x, base=16) != 0:
                x = int(x, base=16)
        if 'ABS_MT_POSITION_Y' in line:
            # 字符串去掉空格后转化为list
            lsy = line.strip().split(' ')
            # 取list中最后一位
            y = lsy[-1]
            # 将16进制转化为10进制
            if int(y, base=16) != 0:
                y = int(y, base=16)
                # print(x,y)
                # 将坐标放到list中
                locs.append((x, y))
                print(locs)
#
for loc in locs:
    print(loc)
    click_event = 'adb shell input tap '
    # 字符串拼接 执行点击命令
    os.system(f'{click_event} {loc[0]} {loc[1]}')
    time.sleep(1)