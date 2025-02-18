from tkinter import Tk, Button, Label, Frame
from run_clash import run_clash
from run_launcher import run_launcher
from time import sleep
from auto_start import subject
from test1 import test
import share
from running import running
from ctypes import windll

# 禁用 DPI 缩放
windll.shcore.SetProcessDpiAwareness(1)


# 定义按钮功能
def button_result():
    result = run_clash()  # 调用 run_clash 获取返回值
    share.clash = result  # 将返回值保存到共享的变量中


def composite():
    button_result()
    sleep(3)
    run_launcher()
    sleep(1)
    running()
 

# 初始化主窗口
root = Tk()
root.title("NIKKE自动化")
root.geometry("1080x800")
root.configure(bg="#f4f4f4")  # 背景颜色

# 标题
main_label = Label(
    root,
    text="NIKKE 自动化工具",
    font=("微软雅黑", 48, "bold"),
    bg="#f4f4f4",
    fg="#333333",
    pady=20
)
main_label.pack()

# 按钮框架
button_frame = Frame(root, bg="#f4f4f4")
button_frame.pack(pady=30)


# 创建按钮的通用函数
def create_button(parent, text, command, row, column, bg_color="#4CAF50", hover_color="#3E8E41", **grid_kwargs):
    button = Button(
        parent,
        text=text,
        command=command,
        width=12,
        height=2,
        font=("微软雅黑", 16),
        bg=bg_color,  # 默认背景颜色
        fg="white",
        activebackground=hover_color,  # 按钮按下时的背景颜色
        activeforeground="white",
        bd=0,
        relief="flat",
        cursor="hand2"  # 鼠标悬停时显示手形光标
    )
    button.grid(row=row, column=column, padx=15, pady=10, **grid_kwargs)

    # 添加悬停效果
    def on_enter(event):
        button.config(bg=hover_color)

    def on_leave(event):
        button.config(bg=bg_color)

    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)


# 添加按钮
create_button(button_frame, "启动代理", button_result, 0, 0)
create_button(button_frame, "启动登录器", run_launcher, 0, 1)
create_button(button_frame, "进入游戏", running, 1, 0)
create_button(button_frame, "开始收菜", subject, 1, 1)
create_button(button_frame, "一条龙启动", composite, 2, 0, columnspan=2)

# 特殊设计的“测试功能”按钮，红色背景
create_button(
    button_frame,
    "测试功能",
    test,
    3,
    0,
    columnspan=2,
    bg_color="#F44336",  # 红色背景
    hover_color="#D32F2F"  # 鼠标悬停变为更深的红色
)

# 状态栏
status_label = Label(
    root,
    text="© 2025 NIKKE 自动化工具 | Designed by 干净的小周",
    font=("微软雅黑", 12),
    bg="#f4f4f4",
    fg="#777777"
)
status_label.pack(side="bottom", pady=10)

# 启动主循环
root.mainloop()

if __name__ == '__main__':
    print('PyCharm')
