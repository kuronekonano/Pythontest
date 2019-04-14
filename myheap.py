class Heap():
    #初始化生成一个优先队列堆(小顶堆)
    def __init__(self, elist=[]):
        self._elems = list(elist)#
        if elist:#初始化时，对数据进行排序
            self.buildheap()#生成堆的函数

    def buildheap(self):
        end = len(self._elems)#堆大小
        for i in range(end//2, -1, -1):#所有非叶节点，从后向前进行筛选排序
            self.siftdown(self._elems[i], i, end)#参数为，被修改的堆内元素，被修改标号，被修改堆的大小


    def siftdown(self,e,begin,end):#向下调整，使堆按顺序排列
        elems, i, j = self._elems, begin, begin*2+1
        #三个值，分别是，实参堆，被传递值的初始位置，被传递值当前位置的左儿子,因为list是从0开始的，用数组表示堆要从1为根节点开始
        #因此左儿子是原位置*2+1
        while j<end:
            if j+1 < end and elems[j+1] < elems[j]:
                j += 1
            #上面的if表示，如果右儿子比左儿子小，那就换右儿子和当前结点比较
            if e < elems[j]:
                break
            #一旦发现左右儿子中最小的那个比当前值大，说明找到位置了，直接退出while向下调整
            elems[i] = elems[j]
            #这里是将值向上挪，也就是给新值腾出位置，相当于新值的向下调整
            i, j = j, 2*j+1
            #交换下标值，当前标号变为j，而j变为其左儿子
        elems[i] = e
        #找到最终位置之后直接赋值，因为elems列表引用的是实参

    def dequeue(self):#弹出元素，之后利用sifidown恢复顺序
        if self.is_empty():
            raise print("空堆")
        elems = self._elems
        #取出第一个即优先级最高的元素
        e0 = elems[0]
        #弹出最后一个元素再放向下筛选函数中进行筛选
        e = elems.pop()
        if len(elems) > 0:#用e表示0位置的值，代替了本该是头部位置的数，相当于把这个数给除去了
            self.siftdown(e,0,len(elems))
        return e0

    def enqueue(self,e):#插入元素，使用向上筛选进行排序
        self._elems.append(None)
        self.siftup(e, len(self._elems)-1)

    def siftup(self, e, last):#向上调整，恢复顺序
        elems, i, j = self._elems, last, (last-1)//2
        while i > 0 and e < elems[j]:#只要当前值比父节点小
            elems[i] = elems[j]#父节点就向下传
            i, j = j, (j-1)//2#指针上移
        elems[i] = e#最后赋值

    def is_empty(self): #检测收否为空
        return not self._elems

    def peek(self):#返回顶峰值
        if self.is_empty():
            raise PermissionError("in peek")
        return self._elems[0]
