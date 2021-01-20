import os
import time
"""
# 点击
adb shell tap x y
# 输入文本,只能输入英文、数字
adb shell input text content
"""
def get_loc_center(startx, starty, endx, endy):
    x = (endx - startx)/2 + startx
    y = (endy - starty)/2 + starty
    return (x,y)

index_page_loc = get_loc_center(0,1506,180,1594)
create_btn_loc = (846,92)
write_weibo_loc = get_loc_center(574,136,882,248)
content_loc = get_loc_center(30,165,870,284)

submit_loc = get_loc_center(780,62,876,122)


# 点击首页
click_event = 'adb shell input tap '
# 发送文本命令
content_event = 'adb shell input text helloworld'

os.system(f'{click_event} {index_page_loc[0]} {index_page_loc[1]}')
 # 点击➕
os.system(f'{click_event} {create_btn_loc[0]} {create_btn_loc[1]}')
time.sleep(2)

# 点击写微博
os.system(f'{click_event} {write_weibo_loc[0]} {write_weibo_loc[1]}')
time.sleep(2)

# 点击输入框
os.system(f'{click_event} {content_loc[0]} {content_loc[1]}')

# 输入文本
os.system(f'{content_event}')

# 点击发送
os.system(f'{click_event} {submit_loc[0]} {submit_loc[1]}')

