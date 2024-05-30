import os
import tkinter as tk
from PIL import Image, ImageTk
import pygame
"""
事件 Event

<Button-1>   鼠标左键
<Button-2>   鼠标中间键（滚轮）
<Button-3>   鼠标右键
<Double-Button-1>   双击鼠标左键
<Double-Button-3>   双击鼠标右键
<Triple-Button-1>   三击鼠标左键
<Triple-Button-3>   三击鼠标右键
<B1-Motion>   鼠标左键滑动
<B2-Motion>   鼠标滚轮移动
<B3-Motion>   鼠标右键滑动

键盘事件
<Key>  event.char
"""
w, h = 100, 100
x, y = 1000, 700
root = tk.Tk()
root.geometry("%dx%d+%d+%d" % (w, h, x, y))  # 定位：width*height+x+y
pygame.init()
# 要想让窗口无边框，你可以使用 overrideredirect 方法，并将其设置为 True：
# 由于窗口没有边框，因此用户无法通过常规方式（例如点击窗口右上角的关闭按钮）来关闭窗口。因此，你可能需要在窗口中添加一个按钮或者其他的交互方式，以便用户可以关闭窗口。
root.overrideredirect(True)
# 将窗口背景色设置为透明 -transparent 是一个选项，用于指定要将哪个颜色设置为透明。  'black' 是一个颜色值，用于指定要将哪个颜色设置为透明
root.attributes('-transparent', 'black')
# -topmost 是一个选项，用于指定要将窗口设置为始终在最上面
root.attributes('-topmost', True)

wali = Image.open("wali.png")  # 打开图片
wali = ImageTk.PhotoImage(wali)  # 转为tkinter的图片格式

canvas = tk.Canvas(root, bg="black")
canvas.pack(fill=tk.BOTH, expand=True)


label = tk.Label(canvas, image=wali)
label.pack()

def on_key_press(event):
    print("按键：", event.char)
    if event.char in ('q', 'Q'):
        exit()
    if event.char in ('c', 'C'):
        os.system("control")  # 打开window应用软件  control   calc
    if event.char in ('m', 'M'):
        pygame.mixer.music.load("Yanni - Nightingale.mp3")
        pygame.mixer.music.play()
    if event.char in ('s', 'S'):
        pygame.mixer.music.stop()

def get_mouse_pos(event):
    global x, y
    x = event.x
    y = event.y


def get_mouse_move(event):
    print(event.x, event.y, root.winfo_x(), root.winfo_y())
    nx = event.x - x + root.winfo_x()
    ny = event.y - y + root.winfo_y()
    root.geometry("%dx%d+%d+%d" % (w, h, nx, ny))


def ani():
    global x
    x -= 2
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))
    root.after(300, ani)


def move(event):
    ani()

# 键盘事件绑定
root.bind('<Key>', on_key_press)
root.bind('<Button-1>', get_mouse_pos)
root.bind('<Button-3>', move)
root.bind('<B1-Motion>', get_mouse_move)


root.mainloop()
