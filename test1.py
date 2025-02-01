from pyautogui import locateOnScreen, ImageNotFoundException, moveTo, click, press
from time import sleep
from run_clash import run_clash
from run_launcher import run_launcher
import share
from auto_start_part import receive_home, sham_battle, store, result_part, NIKKE_result, ark, paid_store


def test():
    # 这里可能要弄一个任务栏中转，version

    sleep(1)
    while not share.stop_event.is_set():
        if paid_store():
            break


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
