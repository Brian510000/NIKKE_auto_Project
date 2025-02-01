from time import sleep
from win32gui import FindWindow, SetWindowPos
from win32con import HWND_TOPMOST, SWP_SHOWWINDOW
# from pyautogui import locateOnScreen, ImageNotFoundException, moveTo, click
# from win32process import GetWindowThreadProcessId
# from psutil import Process
from runningpart import find_x, find_serve, find_sys_error, enter_game
from threading import Thread, Event
import share


def running():
    while not share.stop_event.is_set():  # 当 stop_event 没有被设置时，继续运行
        sleep(5)
        share.hwnd_game = FindWindow("UnityWndClass", "NIKKE")
        if share.hwnd_game:
            print("找到游戏主体句柄了")
            SetWindowPos(share.hwnd_game, HWND_TOPMOST, 0, 0, 1920, 1080, SWP_SHOWWINDOW)
            print("置顶了")
            sleep(5)

            while not share.stop_event.is_set():
                if find_x():
                    break
            while not share.stop_event.is_set():
                if find_serve():
                    while not share.stop_event.is_set():
                        if enter_game():
                            break
                    break  # 退出外层循环，避免重复检查
                elif enter_game():
                    break  # 直接退出外层循环
            break

        else:
            print("没有找到游戏句柄")
            # _, pid = GetWindowThreadProcessId(share.hwnd_game)
            # process = Process(pid)
            # print(process)
            # process.kill()
            # 蜜汁操作，没有找到游戏句柄，我结束个毛的进程啊
            sleep(1)


def sys_error_circulation():
    while True:
        if find_sys_error():
            break
    sleep(1)
    running()


system_error = Thread(target=sys_error_circulation)
system_error.start()
print("1234")
'''
hwnd_game = FindWindow("UnityWndClass", "NIKKE")

if hwnd_game:
    print("find")
    sleep(1)
    SetWindowPos(hwnd_game, HWND_TOPMOST, 0, 0, 1280, 900, SWP_SHOWWINDOW)
'''

'''
开发者笔记
先赠送好友点数
收菜
基地
模拟战
'''
