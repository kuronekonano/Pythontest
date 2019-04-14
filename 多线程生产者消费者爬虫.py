import ctypes
import inspect
import queue
import re
import threading
import time
import tkinter
import tkinter as tk
import urllib.request
from json import loads
from tkinter import scrolledtext
from tkinter import *
thread_que = queue.Queue()
myqueue = queue.Queue()
lock = threading.Lock()
count = 0


def spider_boxoffice():
    url = 'https://box.maoyan.com/promovie/api/box/second.json'
    page = urllib.request.urlopen(url)
    html_code = page.read()
    model_dict = loads(html_code.decode('utf-8'))
    serverTime = model_dict['data']['serverTime']
    totalBox = model_dict['data']['totalBox']
    totalBoxUnit = model_dict['data']['totalBoxUnit']
    Info = 'time：%s total：%s %s\n' % (serverTime, totalBox, totalBoxUnit)
    scr1.insert(tk.END, Info)
    myqueue.put(Info)
    for elem in model_dict['data']['list']:
        movieName = elem['movieName']
        boxInfo = elem['boxInfo']
        boxRate = elem['boxRate']
        showInfo = elem['showInfo']
        showRate = elem['showRate']
        avgShowView = elem['avgShowView']
        avgSeatView = elem['avgSeatView']
        Info = '电影：%s 总票房(万)：%s 票房占比：%s 排片场次：%s 排片占比：%s 场均人次：%s 上座率：%s\n' % (
            movieName, boxInfo, boxRate, showInfo, showRate, avgShowView, avgSeatView)
        scr1.insert(tk.END, Info)
        myqueue.put(Info)

def spider_weobo():
    url = 'https://s.weibo.com/top/summary?cate=socialevent'
    page = urllib.request.urlopen(url)
    html_code = page.read()
    pattern = re.compile(r'<a href=".+?" target="_blank">(.+?)<')
    result = pattern.findall(html_code.decode('utf-8'), 0)
    for ite in result:
        Info = '%s\n'%ite
        scr1.insert(tk.END, Info)
        myqueue.put(Info)
# 线程终止==============================================================================


def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
        tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)
# ====================================================================================


def producer(id):
    global count
    while True:
        lock.acquire()
        count += 1
        Info = 'No. [%d] producer  out [%d]\n'% (id, count)
        scr1.insert(tk.END, Info)
        myqueue.put(Info)
        lock.release()
        time.sleep(0.5)


def customer(id):
    while True:
        scr2.insert(tk.END, "No.[%d]consumer:%s" % (id, myqueue.get()))
        time.sleep(1)


root = tk.Tk()
root.title("KuroNeko")
root['height'] = 540
root['width'] = 555
# 创建标签==================================================================
label_producer = tk.Label(root, text='producer:', justify=tk.RIGHT,fg='red')#标签文本内容，标签
label_producer.place(x=10, y=10, width=70, height=25)

label_customer = tk.Label(root, text='consumer:', justify=tk.RIGHT,fg='green')
label_customer.place(x=120, y=10, width=70, height=25)

label_customer = tk.Label(root, text='producer', justify=tk.RIGHT,fg='blue')
label_customer.place(x=10, y=40, width=70, height=25)

label_customer = tk.Label(root, text='consumer', justify=tk.RIGHT,fg='Orchid')
label_customer.place(x=10, y=265, width=70, height=25)
# 创建文本框================================================================
entry_producer = tk.Entry(root)
entry_producer.place(x=80, y=10, width=30, height=25)

entry_customer = tk.Entry(root)
entry_customer.place(x=190, y=10, width=30, height=25)

# 创建开始停止按钮===========================================================


def run():
    if entry_producer.get():
        for i in range(int(entry_producer.get())):#获取文本框得到的数据，转换为int型
            t = threading.Thread(target=producer, args=(i,))
            thread_que.put(t)
            t.start()

        for i in range(int(entry_customer.get())):
            t = threading.Thread(target=customer, args=(i,))
            thread_que.put(t)
            t.start()


button_run = tk.Button(root, text='Start', command=run)
button_run.place(x=230, y=10, width=40, height=25)


def stop():

    while not thread_que.empty():
        t = thread_que.get()
        stop_thread(t)


button_stop = tk.Button(root, text='Stop', command=stop)
button_stop.place(x=270, y=10, width=40, height=25)

# 创建滚动文本框==================================================================

scr1 = scrolledtext.ScrolledText(root, font=('幼圆', 13),fg='red')#滚动条字体、颜色
scr1.place(x=10, y=70, width=480, height=150)#大小及位置

scr2 = scrolledtext.ScrolledText(root, font=('微软雅黑', 10),fg='blue')
scr2.place(x=10, y=310, width=480, height=150)

# 爬虫==========================================================================

spider = tk.IntVar()
spider.set(0)

boxoffice = tk.Radiobutton(root, variable=spider, value=0, text='movie')
boxoffice.place(x=330, y=250, width=70, height=25)


weibo = tk.Radiobutton(root, variable=spider, value=1, text='weibo')
weibo.place(x=330, y=15, width=100, height=25)


def crawl():
    if spider.get():
        t = threading.Thread(target=spider_weobo)
        t.start()
    else:
        t = threading.Thread(target=spider_boxoffice)
        t.start()
button_stop = tk.Button(root, text='Start', command=crawl)
button_stop.place(x=420, y=15, width=100, height=25)

def clean():
    scr1.delete(1.0, tk.END)
    scr2.delete(1.0, tk.END)
button_clean = tk.Button(root, text='clean', command=clean)
button_clean.place(x=600, y=10, width=40, height=25)
var = tkinter.StringVar()  # 设置变量
var.set('请选择爬取内容')
root.mainloop()
