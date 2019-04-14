# for line in sys.stdin:#有点意思，Python的while输入方法，先用for循环整行读入到line列表中，然后分隔符序列解包
#     a=line.split()
#     if int(a[0])==int(a[1]) :
#         print(int(a[0]),'==',int(a[1]))
#     elif int(a[0])<int(a[1]):
#         print(int(a[0]),'<',int(a[1]))
#     else:
#         print(int(a[0]),'>',int(a[1]))




# from tkinter import *
# from tkinter import filedialog
# import pygame
#
# pygame.init()
#
#
# def zanting():#暂停方法
#     pygame.mixer.music.pause()
#
#
# def stop():#停止方法
#     pygame.mixer.music.stop()
#
#
# def bofang():#播放方法
#     pygame.mixer.music.unpause()
#
#
# def callback():#选择音乐路径
#     file = filedialog.askopenfilename()
#     print(file)
#
#     # file = ""  # 加上音乐路径
#
#     print("播放音乐")
#
#     track = pygame.mixer.music.load(file)
#     pygame.mixer.music.play()
#
#
# root = Tk()  # 窗口
# root.title("KuroNeko的播放器")  # 标题
#
# root.geometry("400x300+400+200")  # 定义窗口的大小和位置
# me = Menu()  # 一级菜单
# root.config(menu=me)  # 加入一级菜单
# menuf = Menu(me)  # 二级菜单
#
# pygame.init()
# pygame.mixer.init()
#
# l = Label(root, text="欢迎来到KuroNeko的音乐播放器")
# l.pack()
# b = Button(root, text="选择音乐", command=callback)
# b.pack()
#
# f = Button(root, text="暂停", command=zanting)
# f.pack()
# bs = Button(root, text="继续", command=bofang)
# bs.pack()
# bst = Button(root, text="停止", command=stop)
# bst.pack()
# root.mainloop()



# print(r.text)  # 打印解码后的返回数据
# import requests
# response = requests.get("https://www.tgbus.com/Robot.txt")
# with open("1.jpg","wb") as f:
#     f.write(response.content)
# f.close()