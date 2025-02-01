from pyautogui import locateOnScreen, ImageNotFoundException, moveTo, click, moveRel, press
from time import sleep
import share
from random import randint, uniform


def friend():
    print("执行赠送好友点数_查找中")
    num = randint(1, 8)  # 生成 1 到 8 之间的随机整数（包括 1 和 8）
    num_f = uniform(0.1, 0.3)
    try:
        auto1 = locateOnScreen("images/img_23.png", confidence=0.7)
        moveTo(auto1, duration=0.2)
        moveRel(num, num, duration=num_f)
        click()
        sleep(2)
        # 这里也有网络波动延迟
        while not share.stop_event.is_set():
            try:
                locateOnScreen("images/img_56.png", confidence=0.95)
                moveTo(1110, 911, duration=0.2)
                moveRel(num, num, duration=num_f)
                click()
                while not share.stop_event.is_set():
                    try:
                        locateOnScreen("images/img_24.png", confidence=0.7)
                        moveTo(968, 682, duration=0.2)
                        moveRel(num, num, duration=num_f)
                        click()
                        sleep(1)
                        moveTo(1185, 171, duration=0.2)
                        moveRel(num, num, duration=num_f)
                        click()
                        break
                    except ImageNotFoundException:
                        print("Error: 好友收发完毕没有找到 not found.")  # 如果抛出异常，处理并继续
                        sleep(1)
                break
            except ImageNotFoundException:
                print("蓝色的赠送好友未找到")
                sleep(1)
        return 1
    except ImageNotFoundException:
        print("Error: 好友按钮 not found.")  # 如果抛出异常，处理并继续
        sleep(1)
        return 0


def receive_box():
    print("收菜_直接点击,点击玩后要网络波动等待，")
    num = randint(1, 8)  # 生成 1 到 8 之间的随机整数（包括 1 和 8）
    num_f = uniform(0.1, 0.3)
    moveTo(570, 903, duration=0.2)
    moveRel(num, num, duration=num_f)
    click()
    sleep(1)
    while not share.stop_event.is_set():
        try:
            auto2 = locateOnScreen("images/img_22.png", confidence=0.8)
            print("一举歼灭找到了")
            moveTo(auto2, duration=0.2)
            moveRel(num, num, duration=num_f)
            click()
            moveTo(1044, 832, duration=0.3)
            moveRel(num, num, duration=num_f)
            click()
            # 网络波动等待
            while not share.stop_event.is_set():
                try:
                    locateOnScreen("images/img_54.png", confidence=0.7)
                    # 这里也不能找U盘，找reward
                    moveTo(888, 888, duration=0.2)
                    moveRel(num, num, duration=num_f)
                    click()
                    break
                except ImageNotFoundException:
                    print("Error: 一举歼灭的 REWARD not found.")  # 如果抛出异常，处理并继续
                    sleep(1)
            sleep(0.5)
            moveTo(808, 836, duration=0.2)
            moveRel(num, num, duration=num_f)
            click()

            sleep(0.5)
            moveTo(1086, 918, duration=0.2)
            moveRel(num, num, duration=num_f)
            click()
            # 网络波动等待
            sleep(1)
            while not share.stop_event.is_set():
                # 要写if检测，因为可能要指挥官升级
                try:
                    # 珠宝也不是关键图像，先堵住这条路，后面再优化，还有当指挥官升级到整数倍的时候，会弹出露比，购买礼包，关键图像是58
                    print("正在检测是否有指挥官升级关键图像")
                    locateOnScreen("images/3.png", confidence=0.8)
                    print("指挥官升级找到了")
                    moveTo(888, 888, duration=0.2)
                    moveRel(num, num, duration=num_f)
                    click()
                    sleep(1)
                    moveTo(888, 888, duration=0.2)
                    moveRel(num, num, duration=num_f)
                    click()
                    break

                except ImageNotFoundException:
                    print("指挥官升级未找到")
                    try:
                        locateOnScreen("images/img_54.png", confidence=0.8)
                        # 这里不能找U盘，因为他不是关键图像，还是直接找reward吧
                        moveTo(888, 888, duration=0.2)
                        moveRel(num, num, duration=num_f)
                        click()
                        break
                    except ImageNotFoundException:
                        print("Error: 获得奖励的REWARD not found.")  # 如果抛出异常，处理并继续
                        sleep(1)
            break
        except ImageNotFoundException:
            print("Error: 一键歼灭 not found.")  # 如果抛出异常，处理并继续
            sleep(1)
    return 1


def receive_home():
    print("基地——直接点击")
    num = randint(1, 8)  # 生成 1 到 8 之间的随机整数（包括 1 和 8）
    num_f = uniform(0.1, 0.3)
    moveTo(574, 842, duration=0.2)
    moveRel(num, num, duration=num_f)
    click()
    sleep(3)
    # 网络波动等待
    while not share.stop_event.is_set():
        try:
            locateOnScreen("images/img_26.png", confidence=0.8)
            moveTo(998, 1012, duration=0.2)
            moveRel(num, num, duration=num_f)
            click()
            sleep(1)
            # 网络波动等待
            while not share.stop_event.is_set():
                try:
                    auto_4 = locateOnScreen("images/img_27.png", confidence=0.8)
                    moveTo(auto_4, duration=0.2)
                    moveRel(num, num, duration=num_f)
                    click()
                    sleep(1)
                    # 网络波动等待
                    while not share.stop_event.is_set():
                        try:
                            locateOnScreen("images/img_43.png", confidence=0.8)
                            moveTo(888, 888, duration=0.2)
                            moveRel(num, num, duration=num_f)
                            click()
                            print("开始派遣")
                            moveTo(964, 904, duration=0.5)
                            moveRel(num, num, duration=num_f)
                            click()
                            print("派遣")
                            sleep(0.5)
                            moveTo(1047, 911, duration=0.2)
                            moveRel(num, num, duration=num_f)
                            click()
                            sleep(1)
                            # 网络波动等待
                            while not share.stop_event.is_set():
                                try:
                                    locateOnScreen("images/img_28.png", confidence=0.8)
                                    moveTo(1198, 184, duration=0.2)
                                    click()
                                    sleep(1)
                                    moveTo(1673, 149, duration=0.2)
                                    moveRel(num, num, duration=num_f)
                                    click()
                                    print("点击任务栏了")
                                    # 这里有网络波动
                                    sleep(1.5)
                                    while not share.stop_event.is_set():
                                        try:
                                            locateOnScreen("images/img_30.png", confidence=0.8)
                                            moveTo(1142, 878, duration=0.2)
                                            moveRel(num, num, duration=num_f)
                                            click()
                                            break
                                        except ImageNotFoundException:
                                            print("任务栏的全部领取未找到")
                                            sleep(1)
                                    break
                                    # 有网络波动等待，交给下一个函数吧
                                except ImageNotFoundException:
                                    print("灰色的全部派遣没有找到")
                                    sleep(1)
                            break
                        except ImageNotFoundException:
                            print("没有找到珠宝，可能没有reward成功")
                            sleep(1)
                    break
                except ImageNotFoundException:
                    print("全部领取 not found")
                    sleep(1)
            break
        except ImageNotFoundException:
            print("Error: 指挥官室 not found.")  # 如果抛出异常，处理并继续
            sleep(1)
    return 1


def sham_battle():
    print("模拟战——查找中")
    num = randint(1, 8)  # 生成 1 到 8 之间的随机整数（包括 1 和 8）
    num_f = uniform(0.1, 0.3)
    try:
        auto_5 = locateOnScreen("images/img_29.png", confidence=0.8)
        sleep(0.5)
        moveTo(auto_5, duration=0.2)
        moveRel(num, num, duration=num_f)
        click()
        sleep(1)
        moveTo(1092, 916, duration=0.2)
        moveRel(num, num, duration=num_f)
        click()
        sleep(2)
        # 网络波动等待
        while not share.stop_event.is_set():
            try:
                auto_6 = locateOnScreen("images/img_31.png", confidence=0.8)
                moveTo(auto_6, duration=0.2)
                moveRel(num, num, duration=num_f)
                click()
                sleep(2)
                moveTo(1100, 1000, duration=0.2)
                moveRel(num, num, duration=num_f)
                click()
                print("开始战斗了")
                sleep(15)
                while not share.stop_event.is_set():
                    try:
                        auto_7 = locateOnScreen("images/img_32.png", confidence=0.8)
                        moveTo(auto_7, duration=0.2)
                        moveRel(num, num, duration=num_f)
                        click()
                        sleep(2)
                        # 又是网络波动等待
                        while not share.stop_event.is_set():
                            try:
                                auto_8 = locateOnScreen("images/img_33.png", confidence=0.8)
                                moveTo(auto_8, duration=0.2)
                                moveRel(num, num, duration=num_f)
                                click()
                                sleep(1)
                                moveTo(954, 688, duration=0.2)
                                moveRel(num, num, duration=num_f)
                                click()
                                sleep(1)
                                # 这里不能简单的moveto
                                # moveTo(162, 1019, duration=0.2)
                                # moveRel(num, num, duration=num_f)
                                # click()
                                while not share.stop_event.is_set():
                                    try:
                                        auto_15 = locateOnScreen("images/img_55.png", confidence=0.8)
                                        moveTo(auto_15, duration=0.2)
                                        click()
                                        break
                                    except ImageNotFoundException:
                                        print("没有找到回到主页按钮")
                                        sleep(1)
                                print("回到主页面中，有网络波动等待")
                                break
                            except ImageNotFoundException:
                                print("没有找到模拟结束")
                                sleep(1)
                        break
                    except ImageNotFoundException:
                        print("没有找到点击任意处进行下一步，可能还在战斗中")
                        sleep(2)
                break
            except ImageNotFoundException:
                print("没有找到跳过全部增益")
                sleep(1)
        return 1
    except ImageNotFoundException:
        print("开始模拟没有找到")
        sleep(1)
        return 0


def store():
    print("正在检查是否回到了主页面")
    num = randint(1, 8)  # 生成 1 到 8 之间的随机整数（包括 1 和 8）
    num_f = uniform(0.1, 0.3)
    try:
        locateOnScreen("images/img_23.png", confidence=0.8)
        print("回到主页面了，接下来点击商店")
        moveTo(586, 747, duration=0.2)
        moveRel(num, num, duration=num_f)
        click()
        # 好像 无 网络波动等待
        sleep(3)
        moveTo(238, 751, duration=0.2)
        moveRel(num, num, duration=num_f)
        click()
        sleep(1)
        moveTo(1054, 910, duration=0.2)
        moveRel(num, num, duration=num_f)
        click()
        sleep(1)
        moveTo(888, 888, duration=0.2)
        moveRel(num, num, duration=num_f)
        click()
        print("点击任意键完毕了")
        sleep(1)
        moveTo(327, 511, duration=0.2)
        click()
        sleep(1)
        moveTo(1082, 686, duration=0.2)
        moveRel(num, num, duration=num_f)
        click()
        sleep(1)
        # 网络波动等待
        while not share.stop_event.is_set():
            try:
                locateOnScreen("images/img_57.png", confidence=0.8)
                moveTo(238, 751, duration=0.2)
                moveRel(num, num, duration=num_f)
                click()
                sleep(1)
                moveTo(1054, 910, duration=0.2)
                moveRel(num, num, duration=num_f)
                click()
                sleep(1)
                moveTo(888, 888, duration=0.2)
                moveRel(num, num, duration=num_f)
                click()
                sleep(1)
                break
            except ImageNotFoundException:
                print("等待商店刷新完毕中")
                sleep(1)
        print("初始商店购买完毕了")
        moveTo(52, 687, duration=0.2)
        moveRel(num, num, duration=num_f)
        click()
        sleep(1)
        moveTo(698, 751, duration=0.2)
        moveRel(num, num, duration=num_f)
        click()
        sleep(1)
        moveTo(1054, 890, duration=0.2)
        moveRel(num, num, duration=num_f)
        click()
        sleep(1)
        while not share.stop_event.is_set():
            try:
                locateOnScreen("images/img_34.png", confidence=0.8)
                # 也可以使用reward，等后面再优化吧
                moveTo(888, 888, duration=0.2)
                moveRel(num, num, duration=num_f)
                click()
                break
            except ImageNotFoundException:
                print("橙色自选箱没有找到，如果在这里循环，前面的购买就一定出错了")
                sleep(1)
        sleep(1)
        print("准备点击返回主页了")
        moveTo(166, 1012, duration=0.2)
        click()
        sleep(1)
        return 1
    except ImageNotFoundException:
        print("没有找到好友按钮")
        sleep(1)
        return 0


def result_part():
    # 总共有3种状态
    # 一种是已经满的，但是这个可以和正常快速一样执行
    # 一种是还没有过五次的，得单独检测
    # 或者直接统一，都手动咨询
    # 还有，有的咨询过后有升级
    # 任意点击可以888
    # 有些咨询是点两下1的，可以循环检测按钮是否存在
    # 每次咨询都要按一下LSHIFT
    # img38应该会更好检测
    # 按1过后可以检测跳过键是否存在，如果存在直接跳过，不存在则继续等，然后再按1，直接接]
    i = 0
    print("咨询检测函数正在运行中")
    while not share.stop_event.is_set():
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
            while not share.stop_event.is_set():
                try:
                    auto_9 = locateOnScreen("images/img_47.png", confidence=0.8)
                    print("已经找到Lshift键了")
                    moveTo(auto_9, duration=0.2)
                    moveRel(num, num, duration=num_f)
                    click()
                    sleep(4)
                    while not share.stop_event.is_set():
                        try:
                            print("找2键")
                            locateOnScreen("images/img_38.png", confidence=0.8)
                            sleep(0.2)
                            press('1')
                            sleep(1)
                            press(']')
                            sleep(1)
                            i += 1
                            share.i = i
                            print(f"目前执行了{share.i}次")
                            while not share.stop_event.is_set():
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
                                    locateOnScreen("images/img_48.png", confidence=0.95)
                                    # 测试
                                    print("咨询键变亮了，已经到达下一位角色")
                                    break
                                except ImageNotFoundException:
                                    print("咨询键未变亮，继续循环找")
                                    sleep(1)
                                if share.i == 9:
                                    print("最后一次了，等待四秒")
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
                                    break
                            break
                        except ImageNotFoundException:
                            print("没有找到选项2，等待中")
                            sleep(1)
                    break
                except ImageNotFoundException:
                    print("没有检测到Lshift按钮，可能没进入聊天页面")
                    sleep(1)
            if share.i == 9:
                break
        except ImageNotFoundException:
            print("没有找到咨询按钮")
        print(f"咨询函数运行成功{share.i}次")


def NIKKE_result():
    print("准备开始咨询妮姬了，先检测是否在主页面")
    num = randint(1, 8)  # 生成 1 到 8 之间的随机整数（包括 1 和 8）
    num_f = uniform(0.1, 0.3)
    try:
        locateOnScreen("images/img_23.png", confidence=0.8)
        print("回到主页面了")
        moveTo(759, 989, duration=0.2)
        moveRel(num, num, duration=num_f)
        click()
        sleep(2)
        moveTo(1672, 170, duration=0.2)
        moveRel(num, num, duration=num_f)
        click()
        sleep(1)
        # 这里是有网络波动延迟的
        while not share.stop_event.is_set():
            try:
                locateOnScreen('images/img_45.png', confidence=0.95)
                print("找到咨询列表了")
                moveTo(460, 400, duration=0.2)
                moveRel(num, num, duration=num_f)
                click()
                sleep(1)
                # 从这里插入函数
                # for i in range(1, 10):
                #     share.i = i
                result_part()
                # print(f"目前执行了{i}次")
                # sleep(0.5)
                print("现在返回主页面")
                moveTo(164, 1017, duration=0.2)
                click()
                break
            except ImageNotFoundException:
                print("没有找到咨询列表")
                sleep(1)

        """
        # 废弃方案
        moveTo(1080, 820, duration=0.2)
        moveRel(num, num, duration=num_f)
        click()
        sleep(1)
        moveTo(1088, 686, duration=0.2)
        moveRel(num, num, duration=num_f)
        click()
        sleep(1)
        # 点击完快速咨询的确定后，有网络波动
        """
        return 1
    except ImageNotFoundException:
        print("没有检测到好友按钮")
        sleep(1)
        return 0


def intercept():
    k = 0
    num = randint(1, 8)  # 生成 1 到 8 之间的随机整数（包括 1 和 8）
    num_f = uniform(0.1, 0.3)
    print("开始检测页面是否在拦截战斗主页")
    while not share.stop_event.is_set():
        try:
            locateOnScreen("images/img_52.png", confidence=0.8)
            sleep(1)
            moveTo(960, 880, duration=0.2)
            moveRel(num, num, duration=num_f)
            click()
            sleep(2)
            moveTo(1100, 990, duration=0.2)
            moveRel(num, num, duration=num_f)
            click()
            sleep(200)
            print("正在循环检测是否通关")
            while not share.stop_event.is_set():
                try:
                    auto_13 = locateOnScreen("images/img_32.png", confidence=0.8)
                    sleep(1)
                    moveTo(auto_13, duration=0.2)
                    moveRel(num, num, duration=num_f)
                    click()
                    sleep(1)
                    # 网络波动
                    while not share.stop_event.is_set():
                        try:
                            auto_14 = locateOnScreen("images/img_53.png", confidence=0.8)
                            sleep(0.5)
                            moveTo(auto_14, duration=0.2)
                            moveRel(num, num, duration=num_f)
                            click()
                            sleep(1)
                            # 点击快速战斗后，也有网络波动
                            while not share.stop_event.is_set():
                                try:
                                    locateOnScreen("images/img_32.png", confidence=0.8)
                                    moveTo(auto_13, duration=0.2)
                                    moveRel(num, num, duration=num_f)
                                    click()
                                    k += 1
                                    break
                                except ImageNotFoundException:
                                    print("没有找到点击任意退出")
                                    sleep(1)
                            if k == 2:
                                break
                            print("已经执行快速战斗一次了")
                            sleep(1)
                        except ImageNotFoundException:
                            print("快速战斗未找到")
                            sleep(1)
                    break
                except ImageNotFoundException:
                    print("没有检测到通关的关键图像")
                    sleep(2)
            break
        except ImageNotFoundException:
            print("没有找到拦截主页关键图像（克拉肯）")
            sleep(1)


def ark():
    print("先检测是否在主页，然后进入方舟领取奖励，再进行拦截战斗")
    num = randint(1, 8)  # 生成 1 到 8 之间的随机整数（包括 1 和 8）
    num_f = uniform(0.1, 0.3)
    j = 0
    try:
        locateOnScreen("images/img_23.png", confidence=0.8)
        print("回到主页面了")
        sleep(1)
        moveTo(1335, 737, duration=0.2)
        moveRel(num, num, duration=num_f)
        click()
        print("已点击进入方舟")
        sleep(1)
        # 这一段循环是领取竞技场奖励
        while not share.stop_event.is_set():
            try:
                auto_11 = locateOnScreen("images/img_49.png", confidence=0.8)
                moveTo(auto_11, duration=0.2)
                moveRel(num, num, duration=num_f)
                click()
                sleep(1)
                # 网络波动延迟
                while not share.stop_event.is_set():
                    try:
                        auto_12 = locateOnScreen("images/img_50.png", confidence=0.8)
                        moveTo(auto_12, duration=0.2)
                        moveRel(num, num, duration=num_f)
                        click()
                        print("找到领取了，已点击")
                        sleep(1)
                        # 网络波动延迟
                        while not share.stop_event.is_set():
                            try:
                                locateOnScreen("images/img_51.png", confidence=0.8)
                                moveTo(888, 888, duration=0.2)
                                moveRel(num, num, duration=num_f)
                                click()
                                break
                            except ImageNotFoundException:
                                print("没有找到REWARD")
                                sleep(1)
                        break
                    except ImageNotFoundException:
                        print("没有找到领取的按钮")
                        sleep(1)
                break
            except ImageNotFoundException:
                print("没有找到要领取的奖励")
                j += 1
                sleep(1)
            if j == 5:
                break
        sleep(1)
        print("然后执行拦截者函数，先点击进入拦截战主页")
        moveTo(895, 841, duration=0.2)
        moveRel(num, num, duration=num_f)
        click()
        intercept()
        sleep(1)
        print("OK!准备返回主页")
        moveTo(169, 1015, duration=0.2)
        click()
        return 1
    except ImageNotFoundException:
        print("检测到没有在主页")
        sleep(1)
        return 0


def paid_store():
    print("先检测是否在主页，然后进入付费商店领取奖励")
    num = randint(1, 8)  # 生成 1 到 8 之间的随机整数（包括 1 和 8）
    num_f = uniform(0.1, 0.3)
    try:
        locateOnScreen("images/img_23.png", confidence=0.8)
        print("回到主页面了")
    except ImageNotFoundException:
        print("没有找到好友按钮，不在主页面")
        sleep(1)
        return 0
    print("开始点击付费商店")
    sleep(1)
    moveTo(595, 681, duration=0.2)
    moveRel(num, num, duration=num_f)
    click()
    sleep(1.5)
    while not share.stop_event.is_set():
        try:
            auto_18 = locateOnScreen("images/img_59.png", confidence=0.8)
            moveTo(auto_18, duration=0.2)
            moveRel(num, num, duration=num_f)
            click()
            break
        except ImageNotFoundException:
            print("can't not find the present with a red dot")
            sleep(1)
    sleep(1)
    moveTo(266, 337, duration=0.2)
    moveRel(num, num, duration=num_f)
    click()
    sleep(1)
    moveTo(154, 691, duration=0.2)
    moveRel(num, num, duration=num_f)
    click()
    sleep(1)
    while not share.stop_event.is_set():
        try:
            locateOnScreen("images/img_60.png", confidence=0.8)
            moveTo(888, 888, duration=0.2)
            moveRel(num, num, duration=num_f)
            click()
            break
        except ImageNotFoundException:
            print("can't not find the REWARD")
            sleep(1)
    sleep(1)
    while not share.stop_event.is_set():
        try:
            auto_19 = locateOnScreen("images/img_55.png", confidence=0.8)
            moveTo(auto_19, duration=0.2)
            click()
            break
        except ImageNotFoundException:
            print("can't not find HOME")
            sleep(1)
    return 1
