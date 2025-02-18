from pyautogui import locateOnScreen, ImageNotFoundException, moveTo, click, press, moveRel
from time import sleep
from run_clash import run_clash
from run_launcher import run_launcher
import share
from auto_start_part import receive_home, sham_battle, store, result_part, NIKKE_result, ark, paid_store
from random import randint, uniform

def test():
    # 这里可能要弄一个任务栏中转，version
    # 初始化或获取共享资源中的停止事件，用于控制循环的终止
    # while True:

    #     sleep(1)  # 让当前线程暂停1秒钟
    #     # 等待1秒后开始执行主循环
    #     try:
    #         locateOnScreen("images/img_32.png", confidence=0.8)
    #         print("找到了32")
    #         press('T')

    #     except ImageNotFoundException:
    #         print("继续找")
    #         sleep(1)
    i = 0
    print("咨询检测函数正在运行中")
    while True:
        num = randint(1, 8)  # 生成 1 到 8 之间的随机整数（包括 1 和 8）
        num_f = uniform(0.1, 0.3)
        try:
            # 首先是检测关键图像，是否在咨询界面
            auto_8 = locateOnScreen("images/img_46.png", confidence=0.9)
            print("找到咨询按钮了")
            moveTo(auto_8, duration=0.2)
            moveRel(num, num, duration=num_f)
            click()
            sleep(1)
            moveTo(1087, 687, duration=0.2)
            moveRel(num, num, duration=num_f)
            click()
            sleep(1)
            # 可能有网络波动，要检测是否真的进入聊天页面，然后循环检测图像2是否存在
            while True:
                try:
                    auto_9 = locateOnScreen("images/img_47.png", confidence=0.8)
                    print("已经找到Lshift键了")
                    moveTo(auto_9, duration=0.2)
                    moveRel(num, num, duration=num_f)
                    click()
                    sleep(4)
                    while True:
                        # try:
                        #     print("找2键")
                        #     locateOnScreen("images/img_38.png", confidence=0.8)
                        #     sleep(0.2)
                        #     press('1')
                        #     sleep(1)
                        #     press(']')
                        #     sleep(1)
                        #     i += 1
                        #     share.i = i
                        #     print(f"目前执行了{share.i}次")
                        #     while not share.stop_event.is_set():
                        #         try:
                        #             print("找追加能力值，就是咨询完升级的页面")
                        #             locateOnScreen("images/img_36.png", confidence=0.8)
                        #             print("妮姬好感升级了")
                        #             sleep(1)
                        #             moveTo(888, 888, duration=0.2)
                        #             moveRel(num, num, duration=num_f)
                        #             click()
                        #             sleep(0.5)
                        #         except ImageNotFoundException:
                        #             print("这次没有找到，接下来找右划键")
                        #         try:
                        #             print("找右划键")
                        #             auto_10 = locateOnScreen("images/img_40.png", confidence=0.8)
                        #             sleep(0.5)
                        #             moveTo(auto_10, duration=0.2)
                        #             moveRel(num, num, duration=num_f)
                        #             click()
                        #             sleep(1)
                        #         except ImageNotFoundException:
                        #             print("没有找到右划键")
                        #             sleep(1)
                        #         # 咨询键盘重新变蓝色我再break
                        #         try:
                        #             sleep(1)
                        #             locateOnScreen("images/img_48.png", confidence=0.95)
                        #             # 测试
                        #             print("咨询键变亮了，已经到达下一位角色")
                        #             break
                        #         except ImageNotFoundException:
                        #             print("咨询键未变亮，继续循环找")
                        #             sleep(1)
                        #         if share.i == 9:
                        #             print("最后一次了，等待四秒")
                        #             sleep(4)
                        #             moveTo(600, 300, duration=0.2)
                        #             moveRel(num, num, duration=num_f)
                        #             click()
                        #             moveTo(600, 300, duration=0.2)
                        #             moveRel(num, num, duration=num_f)
                        #             click()
                        #             moveTo(600, 300, duration=0.2)
                        #             moveRel(num, num, duration=num_f)
                        #             click()
                        #             break
                        #     break
                        # except ImageNotFoundException:
                        #     print("没有找到选项2，等待中")
                        #     sleep(1)
                        print("循环按1")
                        sleep(0.2)
                        press('1')
                        sleep(1)
                        press(']')
                        sleep(1)
                        i += 1
                        share.i = i
                        print(f"目前执行了{share.i}次")
                        try:
                            print("找追加能力值，就是咨询完升级的页面")
                            locateOnScreen("images/img_36.png", confidence=0.8)
                            print("妮姬好感升级了")
                            sleep(1)
                            moveTo(888, 888, duration=0.2)
                            moveRel(num, num, duration=num_f)
                            click()
                            sleep(0.5)
                        except ImageNotFoundException:
                            print("这次没有找到，接下来找右划键")
                            sleep(0.5)
                        try:
                            print("找右划键")
                            auto_10 = locateOnScreen("images/img_40.png", confidence=0.8)
                            sleep(0.5)
                            moveTo(auto_10, duration=0.2)
                            moveRel(num, num, duration=num_f)
                            click()
                            sleep(1)
                        except ImageNotFoundException:
                            print("没有找到右划键")
                            sleep(1)
                        # 咨询键盘重新变蓝色我再break
                        try:
                            sleep(1)
                            locateOnScreen("images/img_48.png",confidence=0.95)
                            # 测试
                            print("咨询键变亮了，已经到达下一位角色")
                            break
                        except ImageNotFoundException:
                            print("咨询键未变亮，继续循环找")
                            sleep(1)
                        try:
                            locateOnScreen("images/img_62.png",confidence=0.99)
                            print("已完成全部咨询")
                            sleep(4)
                            moveTo(600, 300, duration=0.2)
                            moveRel(num, num, duration=num_f)
                            click()
                            moveTo(600, 300, duration=0.2)
                            moveRel(num, num, duration=num_f)
                            click()
                            moveTo(600, 300, duration=0.2)
                            moveRel(num, num, duration=num_f)
                            click()
                            share.i = 999
                            break
                        except ImageNotFoundException:
                            print("未咨询完全部角色，继续循环")
                            sleep(1)
                    break
                except ImageNotFoundException:
                    print("没有检测到Lshift按钮，可能没进入聊天页面")
                    sleep(1)
            if share.i == 999:
                break
        except ImageNotFoundException:
            print("没有找到咨询按钮")
        print(f"咨询函数运行成功{share.i}次")




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
