from pyautogui import locateOnScreen, ImageNotFoundException, moveTo, click
from time import sleep
from run_clash import run_clash
from run_launcher import run_launcher
from win32process import GetWindowThreadProcessId
from psutil import Process, NoSuchProcess
from threading import Event
import share

# 创建一个线程事件
share.stop_event = Event()


def find_sys_error():
    print("多线程正常运行中")
    try:
        find_error = locateOnScreen("images/img_20.png", confidence=0.9)
        # 容易误找，想办法改一下图片或者其他
        # moveTo(964, 711, duration=0.2)
        # click()
        if find_error:
            print("找到系统错误了")
            share.stop_event.set()
            print(share.stop_event)
            moveTo(find_error)
            _, pid = GetWindowThreadProcessId(share.hwnd_game)
            try:
                process = Process(pid)
                process.kill()
                sleep(3)
                run_clash()
                sleep(1)
                run_launcher()
                share.stop_event.clear()
                return 1
            except NoSuchProcess:
                print(f"Process PID {pid} not found or has terminated.无PID")

    except ImageNotFoundException:
        print("线程2：当前网络正常，ip地址异常导致系统错误未找到")  # 如果抛出异常，处理并继续
        sleep(1)
    sleep(3)


def find_x():
    try:
        enter1 = locateOnScreen("images/img_18.png", confidence=0.8)
        moveTo(1183, 269, duration=0.2)
        click()
        return 1
    except ImageNotFoundException:
        print("Error: Image公告 not found.")  # 如果抛出异常，处理并继续
        sleep(1)


def find_serve():
    try:
        enter2 = locateOnScreen("images/img_19.png", confidence=0.8)
        moveTo(enter2, duration=0.2)
        click()
        print("找到服务器选择的确认键了")
        return 1
    except ImageNotFoundException:
        print("Error: 服务器 not found.")  # 如果抛出异常，处理并继续
        sleep(1)


def enter_game():
    try:
        entering = locateOnScreen("images/img_21.png", confidence=0.8)
        moveTo(888, 888, duration=0.2)
        click()
        print("点击进入游戏了")
        return 1
    except ImageNotFoundException:
        print("Error: 点击任意键进入游戏 not found.")  # 如果抛出异常，处理并继续
        sleep(1)

def find_downlord():
    try:
        locateOnScreen("images/5.png", confidence=0.8)
        moveTo(1048, 697, duration=0.2)
        click()
        print("找到下载按钮了")
        return 1
    except ImageNotFoundException:
        print("Error: 下载按钮 not found.")  # 如果抛出异常，处理并继续
        sleep(1)