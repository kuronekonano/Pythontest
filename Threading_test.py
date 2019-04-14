import os
import threading
import time
tickis=100  # 声明一个全局变量(全局需要共享数据)存储一辆列车的总票数

# 因为数据存在安全性问题 保证卖票线程不会抢买同一张票 导致售票出问题就需要给数据上锁 从而保证在该票卖了后 再卖其他的
lock=threading.Lock() # threading 提供了锁工具 同样要声明为全局变量

# 定义一个干事情即卖票的函数
def sale_tickis(thread_name):

    global tickis #函数里共享全局变量 需用关键字global声明 否则访问不到
    global lock
    # 卖票
    # 操作数据之前就需要给数据上锁
    while True:
        lock.acquire()
        if tickis!=0:
            tickis-=1
            print(thread_name,"余票为：",tickis)
        else:
            print(thread_name,"票卖完了")
            os._exit(0)   # "0" 表示安全退出 "1"或其他数字表示非正常退出

    # 操作完数据后要释放锁 这样后面才能继续卖票 否则数据锁定则无法卖票
        lock.release()

# 定义一个类创建卖票线程 该类继承自threading.Thread类
class my_thread(threading.Thread):

    def __init__(self,name=""):
        # super(threading.Thread,self).__init__()
        threading.Thread.__init__(self)
        self.name=name
    # 重写Thread类的run()方法以创建线程
    def run(self):
        sale_tickis(self.name) #调用卖票方法

# 初始化类创建线程
if __name__=="__main__":
    for i in range(1,11):
        thread = my_thread("线程" + str(i))
        thread.start()  #开启线程
