import threading

numconsumers = 4
numproducers = 6
nummessages = 4
import _thread as thread, queue, time
safeprint = thread.allocate_lock()
dataQueue = queue.Queue() # 共享全局变量，没有限制大小 可以传参限制大小
def producer(idnum, dataqueue):
    for msgnum in range(nummessages):
        time.sleep(idnum)
        dataqueue.put('[producer id=%d, count=%d]' % (idnum, msgnum)) #放入队列

def consumer(idnum, dataqueue):
    print('-'*20)
    try:
        data = dataqueue.get(block=False) #从队列里取值，如果队列为空者引发异常
    except queue.Empty:
        print('the queue is empty')
        pass
    else:
        with safeprint: #线程锁
            print('consumer', idnum, 'got =>', data)

if __name__ == '__main__':
    for i in range(numproducers):
        waitfor=[]
        thread=threading.Thread(target=producer,args=(i,dataQueue))
        waitfor.append(thread)
        thread.start()
        # thread.start_new_thread(producer, (i, dataQueue))
        # time.sleep(((numproducers-1) * nummessages) + 1) #保证主线程最后退出
    for i in range(numconsumers):
        thread=threading.Thread(target=consumer, args=(i, dataQueue))
        thread.daemon=False
        thread.start()


    for thread in waitfor:thread.join()
    print('Main thread exit.')


# import threading
#
# import queue
# class Producer(threading.Thread):
#    def __init__(self, in_queue, out_queue):
#        threading.Thread.__init__(self)
#        self.in_queue = in_queue
#        self.out_queue = out_queue
#    def run(self):
#        while True:
#            item = self.in_queue.get()
#            result = item
#            self.out_queue.put(result)
#            print('out_queue put',result)
#            self.in_queue.task_done()
# class Consumer(threading.Thread):
#    def __init__(self, out_queue):
#        threading.Thread.__init__(self)
#        self.out_queue = out_queue
#    def run(self):
#        while True:
#            item = self.out_queue.get()
#            result = item
#            self.out_queue.task_done()
# if __name__ == '__main__':
#    item_list = ['item1', 'item2', 'item3']
#    in_queue = queue.Queue()
#    out_queue = queue.Queue()
#    for item in item_list:
#        in_queue.put(item)
#    for i in range(len(item_list)):
#        t = Producer(in_queue, out_queue)
#        t.daemon = True
#        t.start()
#    for i in range(len(item_list)):
#        t = Consumer(out_queue)
#        t.daemon = True
#        t.start()
#    in_queue.join()
#    out_queue.join()