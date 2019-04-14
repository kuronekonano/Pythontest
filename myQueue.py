class myQueue:
    def __init__(self,size=10):#队列容量限定为10个
        self._content=[]#初始空队列
        self._size=size#初始化队里容量
        self._current=0#队首指针
    def setSize(self,size):#设定队列容量
        if size <self._current:#若当前队里内元素数量大于队列容量
            for i in range(size ,self._current)[::-1]:#删除多余元素
                del self._content[i]
            self._current=size#重新标记队首指针
        self._size=size
    def put(self,v):#塞入队列
        if self._current<self._size:#在队列未满的情况下加入元素
            self._content.append(v)#加入新元素到队列存储列表中
            self._current=self._current+1#队首指针后移
        else:
            print('The queue is full')#否则输出队列已满

    def get(self):#获取队首元素
        if self._content:#若列表不为空
            self._current=self._current-1#队首指针-1
            return self._content.pop(0)#返回一个队尾元素
        else:
            print('The queue is empty')#否则输出队列为空
    def show(self):#输出整个队列的所有元素
        if self._content:
            print(self._content)
        else:
            print('The queue is empty')#否则输出队列为空
    def empty(self):#队列清空
        self._content=[]
    def isEmpty(self):#队列是否为空判断
        if not self._content:
            return  True
        else:
            return  False
    def isFull(self):#队列是否为满判断
        if not self._current==self._size:
            return  True
        else:
            return  False
    if __name__=='__main__':
        print('Please use me as moudle.')

# import myQueue
# q=myQueue.myQueue()
# q.get()
# q.put(5)
# q.put(7)
# q.isFull()
# q.put('a')
# q.put(3)
# q.show()