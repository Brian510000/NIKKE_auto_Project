from pyautogui import locateOnScreen, ImageNotFoundException, moveTo, click, press
from time import sleep
from run_clash import run_clash
from run_launcher import run_launcher
import share
from auto_start_part import receive_home, sham_battle, store, result_part, NIKKE_result, ark, paid_store


def test():
    # 这里可能要弄一个任务栏中转，version
    # 初始化或获取共享资源中的停止事件，用于控制循环的终止

    sleep(1)  # 让当前线程暂停1秒钟
    # 等待1秒后开始执行主循环
    try:
        locateOnScreen("images/5.png", confidence=0.8)
        print("找到了5")
    except ImageNotFoundException:
        print("继续找")
        sleep(1)



# while True:
#     try:
#         locateOnScreen("images/img_32.png", confidence=0.8)
#         press('T')
#     except ImageNotFoundException:
#         print("继续找")
#         sleep(1)
#     while True:
#         try:
#             auto = locateOnScreen('images/img_46.png', confidence=0.8)
#             print("找到咨询列表了")
#             moveTo(auto, duration=0.2)
#         except ImageNotFoundException:
#             print("没有找到咨询列表222")
#             sleep(1)
