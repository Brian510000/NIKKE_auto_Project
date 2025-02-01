from subprocess import Popen
from pyautogui import moveTo, click
from win32gui import FindWindow, SetWindowPos
from time import sleep
from win32con import HWND_TOPMOST, SWP_SHOWWINDOW
from launcher_finding import start_game, need_login, internet_error
from run_clash import run_clash
import share

# 初始化


def run_launcher():
    # 启动程序
    launcher = Popen(["E:\\NIKKE\\Launcher\\nikke_launcher.exe"])
    sleep(4)  # 等待程序启动并加载窗口

    # 查找窗口句柄，确保类名和标题都正确
    hwnd_launcher = FindWindow("TWINCONTROL", "NIKKE")  # 如果不知道窗口类名，可以将其设为None，查找窗口标题

    if hwnd_launcher:
        print(f"窗口句柄: {hwnd_launcher}")
        # 如果窗口句柄有效，输出1并进行处理
        print("窗口找到！")
        SetWindowPos(hwnd_launcher, HWND_TOPMOST, 0, 0, 1920, 1080, SWP_SHOWWINDOW)  # 调整窗口大小并置顶

        # 三种情况，1，出现网络错误，此时要重启启动器和launcher
        # 需要登录 moveTo(105, 518, duration=1)
        # 直接启动

        while True:

            if start_game():
                break
            elif need_login():
                break
            elif internet_error():
                print(launcher)
                launcher.kill()
                share.clash.kill()
                sleep(1.5)
                run_clash()
                run_launcher()
                break
            hwnd_launcher = FindWindow("TWINCONTROL", "NIKKE")
            SetWindowPos(hwnd_launcher, HWND_TOPMOST, 0, 0, 1920, 1080, SWP_SHOWWINDOW)  # 调整窗口大小并置顶
            # 可以加一个除非找到nikke本体启动成功，否则继续循环
    else:
        print("未找到窗口")
        # 结束程序
        print(launcher)
        launcher.kill()
        if share.retries < 5:
            print(f"尝试重新启动程序并查找窗口... (第{share.retries + 1}次重试)")
            run_launcher()  # 递归调用，增加重试次数
        else:
            print("已达到最大重试次数，未能找到窗口。")
