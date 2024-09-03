# __init__.py 为初始化加载文件

# 导入系统资源模块
from ascript.android.system import R
# 导入动作模块
from ascript.android import action
# 导入节点检索模块
from ascript.android import node
# 导入图色检索模块
from ascript.android import screen

from ascript.android.action import Selector

# from ascript.android.ui import Device
from ascript.android.system import Device

from ascript.android.ui import Dialog

from ascript.android import system


import time

import random

print("Hello AS!")
Dialog.toast('脚本开始',1000)

def find_search():
    print('find_search')
    # 找到搜索按钮
    # Selector().id("com.ss.android.ugc.aweme:id/jbl").brother(-1).click().find()

    # time.sleep(1)

    # textfield_node = Selector().type("EditText").find()
    # time.sleep(1)
    # if node:
    #     textfield_node.input("自在老师讲的不错")

    # time.sleep(1)

    # action.Hid.key(**a)
    # action.Hid.key(**enter)
    # search_button_node = Selector().id("com.ss.android.ugc.aweme:id/0c+").find()
    # if search_button_node:
    #     search_button_node.click()
    #     print('点击了 search_button_node')
    # else:
    #     print('没有找到search_button_node')


    # keyboard = Device().keyboard()
    # keyboard.press_key("ENTER")
    # #代替点击事件
    # action.click(1127, 170)
    # time.sleep(0.5)
    # action.Key.back()
    

def auto():
    print(f'{count} 新视频================')
    # 页面判断是否可以直接跳过
    live_close_node = Selector().id(
        "com.ss.android.ugc.aweme:id/root").desc("关闭").depth(2).find()
    if live_close_node:
        print('直播间，直接跳过')
        goto_next()
        return
    

    # try:
    #     title_node = Selector().id("com.ss.android.ugc.aweme:id/title").visible(True).find()
    # except:
    #     print('error:title_node')
    #     goto_next()

    # 用户名
    title_node = Selector().id("com.ss.android.ugc.aweme:id/title").visible(True).find()
    if (title_node == None):
        print('title_node No')
        goto_next()
        return
    

    # 评论按钮
    comment_node = Selector().id("com.ss.android.ugc.aweme:id/db4").visible(True).find()
    if(comment_node == None):
        print('comment_node No')
        goto_next()
        return
    
    title = f'{title_node.text}'
    comment = comment_node.desc
    pDialogText = f'title：{title}\n{comment}'
    # print(pDialogText)
    # Dialog.toast(pDialogText,1000)


    if '万' in comment:
        pText = f"{pDialogText}，\n 大大大于一万,"
        print(pText)
        Dialog.toast(pText,1000)
        goto_next()
    else:
        pText = f"{pDialogText}，\n 小小小一万"
        print(pText)
        Dialog.toast(pText,1000)
        comment_node.click()
        time.sleep(1)
        repeat_comment() 

def close_comment_view():
# 关闭评论页面
    try:
        close_comment_node = Selector().id("com.ss.android.ugc.aweme:id/back_btn").visible(True).find()
        close_comment_node.click()
        print('close_comment_node')
    except:
        print(f"error: close_comment_node")

    goto_next()

def repeat_comment():
    print('开始评论')
    temp_count = random.choice([2,3])
    temp_count = 1
    while (temp_count > 0):
        temp_count -= 1
        open_edit_view()

        input_content()

        send_content()

        like_content()
    close_comment_view()    

def open_edit_view():
    try:
        emoji_node = Selector().id("com.ss.android.ugc.aweme:id/k=q").find()
        emoji_node.click()
        print('emoji_node')
        time.sleep(1)
    except:
        print(f"error: emoji_node")


def input_content():
    def _input_text():
        try:
            edit_node = Selector().id("com.ss.android.ugc.aweme:id/c9o").type("EditText").find()
            text_list = ['行动起来  我库库点[猪头] 我很闲，评论最好啦',
                         '活的！！！你干嘛，我干嘛',
                         '宝宝们，你们干嘛 我干嘛',
                         '现在闲的可怕 点了喵[猪头]',
                         '刚刚',
                         '点了一堆 放心嘟嘟[猪头]',
                         '又回完一圈了，超级闲[比心]',
                         '[舔屏][舔屏]活的活的 谁来捡我[舔屏][舔屏]',
                         '刚刚 宝宝们 别刷了就我吧[可怜]',
                         '评论了好多全骗我[流泪]',
                         '刚刚点关注一圈了全是骗人的[流泪]',
                         '行动起来宝宝们，我库库点'
                         ]
            edit_node.input(random.choice(text_list))
            print('edit_node')
            time.sleep(1)
        except:
            print(f"error: edit_node")

    def _input_img():
        #    collect_node = Selector().id("com.ss.android.ugc.aweme:id/w5p").desc("自定义表情").type("Button").depth(7).find()
        collect_node = Selector().type("Button").path(
            "/FrameLayout/FrameLayout/LinearLayout/FrameLayout/RecyclerView/FrameLayout/Button").depth(7).desc("自定义表情").find()
        collect_node.click()
        print('collect_node')
        time.sleep(1)
        huguan_imoji_node = Selector().desc("自定义表情1, 按钮").depth(7).find()
        huguan_imoji_node.click()
        print('huguan_imoji_node')
        time.sleep(1)
    _input_text()

def send_content():
    try:
        #    send_node = Selector().id("com.ss.android.ugc.aweme:id/c-2").type("FrameLayout").depth(5).find()
        # send_node = Selector().id("com.ss.android.ugc.aweme:id/c-6").text("发送").find()
        send_node = Selector().id("com.ss.android.ugc.aweme:id/u7w").text("发送").depth(6).find()
        send_node.click()
        print('send_node')
        time.sleep(2)
    except :
        print(f"error: send_node")


def like_content():
    like_node = Selector().id("com.ss.android.ugc.aweme:id/ex-").clickable(True).visible(True).type("ViewGroup").find()
    like_node.click()
    print('点赞')
    time.sleep(1)


def goto_next():
    time.sleep(1)
    action.slide(610, 2000, 610, 800, 20)
    print('上滑slide')
    time.sleep(3)
    

# auto()  com.ss.android.ugc.aweme:id/root

count = 1000
while count > 0:
    count = count - 1
    
    # print(f"count:{count}")
    auto()

# system.open('微信')   
# time.sleep(2)
# system.exit()
# auto()

# comment_node = Selector().id("com.ss.android.ugc.aweme:id/db4").find()
# print(f'comment:{comment_node.desc}') #评论8.6万，按钮 #评论9426，按钮
# # comment_node.click()
# # time.sleep(1)
# print('comment_node')