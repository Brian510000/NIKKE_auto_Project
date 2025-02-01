from time import sleep
from auto_start_part import friend, receive_box, receive_home, sham_battle, store, NIKKE_result, ark, paid_store
import share


def subject():
    while not share.stop_event.is_set():
        if friend():
            break

    sleep(1)

    while not share.stop_event.is_set():
        if receive_box():
            break

    sleep(1)

    while not share.stop_event.is_set():
        if receive_home():
            break

    # 这里可能要弄一个任务栏中转
    sleep(1)
    while not share.stop_event.is_set():
        if sham_battle():
            break

    # 通过好友按钮检测是否回到了主页面
    sleep(1)
    while not share.stop_event.is_set():
        if store():
            break

    # 同上，检测主页面
    sleep(1)
    while not share.stop_event.is_set():
        if NIKKE_result():
            break

    sleep(1)

    while not share.stop_event.is_set():
        if ark():
            break
    print("!!!大成功！！！别忘记全部领取哟！")

    print("开始额外领取奖励任务")
    while not share.stop_event.is_set():
        if paid_store():
            break
