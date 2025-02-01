from pyautogui import locateOnScreen, ImageNotFoundException, moveTo, write, center, click
from time import sleep


# 查找屏幕上是否存在指定图片

def internet_error():
    print("internet error")
    try:
        locateOnScreen('images/img_41.png', confidence=0.8)
        print("检测到密码错误了，密码错误很可能就是网络错误")
        return 1
    except ImageNotFoundException:
        print("没有检测到网络错误")
        # 如果说检测到网络错误，那直接返回1
        return 0


def need_login():
    try:
        button_location = locateOnScreen('images/2.png', confidence=0.8)
        if button_location:
            print(f"Button found at: {button_location}")

            moveTo(108, 519, duration=0.5)
            click()
            sleep(1)
            write('Brianlm521', interval=0.1)
            moveTo(center(button_location), duration=0.2)
            click()
            sleep(5)
            return 0
        else:
            print("Looking for the button...")  # 未找到时提示
            sleep(0.5)  # 延时0.5秒，避免频繁查找导致资源占用过高
    except ImageNotFoundException:
        print("Error: Image not found.")  # 如果抛出异常，处理并继续
        sleep(0.5)

    # 需要再循环一下句柄，然后移到左上角,这里其实放在start部分就很好了
    # 进行登录操作，delay
    # 然后start_game一下就好了
    # 记得delay


def start_game():
    print("start!!")

    try:
        button_location = locateOnScreen('images/3.png', confidence=0.7)
        if button_location:
            print(f"Button found at: {button_location}")

            moveTo(274, 928, duration=0.5)
            click()

            return 1
        else:  # 这里应该是不进入的，懒得删了
            print("Looking for the button...")  # 未找到时提示
            sleep(0.5)  # 延时0.5秒，避免频繁查找导致资源占用过高

    except ImageNotFoundException:
        print("Error: Image not found.图片3没有找到")
        sleep(0.5)
        return 0
    # 如果图找到了，进行一系列操作然后返回1
    # 没有找到，直接else return 0;
