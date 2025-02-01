from subprocess import Popen
from pyautogui import moveTo, click
from win32gui import FindWindow, SetWindowPos
from time import sleep
from win32con import HWND_TOPMOST, SWP_SHOWWINDOW, HWND_BOTTOM
import share


# win32con 是一个包含许多常用常量的模块，专门用于 win32gui 等 Windows GUI 操作的编程。
def run_clash():
    share.clash = Popen(["D:\\clash\\Clash for Windows.exe"])
    print(f"代理运行的值为: {share.clash}")
    sleep(2.5)
    hwnd_clash = FindWindow("Chrome_WidgetWin_1", "Clash for Windows")
    if hwnd_clash:
        print(f"窗口句柄: {hwnd_clash}")
        sleep(0.1)
        SetWindowPos(hwnd_clash, HWND_TOPMOST, 0, 0, 1280, 900, SWP_SHOWWINDOW)
        sleep(0.1)
        moveTo(130, 366, duration=0.1)
        click()
        moveTo(736, 234, duration=0.2)
        click()
        sleep(1.5)
        SetWindowPos(hwnd_clash, HWND_BOTTOM, 0, 0, 1280, 900, SWP_SHOWWINDOW)
        print(share.clash)
        return share.clash
    else:
        print("未找到窗口")
        share.clash.kill()
        sleep(1)
        if share.retries_clash < 5:
            print(f"尝试重新启动程序并查找窗口... (第{share.retries_clash + 1}次重试)")
            run_clash()  # 递归调用，增加重试次数
        else:
            print("已达到最大重试次数，未能找到窗口。")
