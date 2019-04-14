# coding:utf-8
from tkinter import *
from tkinter import scrolledtext  # 文本滚动条
import threading
import time
from PIL import ImageTk, Image


def count(i):
    for k in range(1, 100 + 1):
        text.insert(END, '第' + str(i) + '线程count:  ' + str(k) + '\n')
        time.sleep(0.001)


def fun():
    for i in range(1, 5 + 1):
        th = threading.Thread(target=count, args=(i,))
        th.setDaemon(True)  # 守护线程
        th.start()
    var.set('创建完毕')


root = Tk()
root.title('个性化gui-1.0')  # 窗口标题
root.geometry('+600+100')  # 窗口呈现位置
image2 = Image.open(r'background.png')
background_image = ImageTk.PhotoImage(image2)
textlabel = Label(root, image=background_image)
textlabel.grid()
text = scrolledtext.ScrolledText(root, font=('微软雅黑', 10), fg='green')
text.grid()
button = Button(root, text='创建线程', font=('微软雅黑', 10), command=fun)
button.grid()
var = StringVar()  # 设置变量
label = Label(root, font=('微软雅黑', 10), fg='yellow', textvariable=var)
label.grid()
var.set('by KuroNeko')
root.mainloop()
