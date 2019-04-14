class Stack:
    def __init__(self,size=10):#栈容量设定为10
        self._content=[]#栈存储列表
        self._size=size#栈容量
        self._current=0#栈顶指针

    def empty(self):#栈清空
        self._content=[]
        self._current=0

    def isEmpty(self):#判断栈是否为空
        if not self._content:
            return True
        else:
            return False

    def setSize(self,size):#判断是否超出栈容量
        if size<self._current:
            for i in range(size,self._current)[::-1]:
                del self._content[i]#超出则删除多余元素
            self._current=size
        self._size=size

    def isFull(self):#判断栈是否为满
        if self._current==self._size:
            return True
        else:
            return False

    def push(self,v):#压栈
        if len(self._content)<self._size:#若栈未满
            self._content.append(v)#压栈
            self._current=self._current+1#栈指针后移
        else:
            print('Stack Full! ')#否则输出栈已满

    def pop(self):#弹出
        if self._content:#若栈内存在元素
            self._current=self._current-1#栈指针-1
            return  self._content.pop()#返回栈顶元素，即最后一位(此处与队列相反)
        else:
            print('Stack Empty! ')#否则输出栈为空

    def show(self):#输出栈内所有元素值
        print(self._content)

    def showRemainderSpace(self):#栈内剩余容量
        print('Stack can still PUSH',self._size-self._current,'elements.')

    if __name__=='__main__':
        import myStack
        s=myStack.Stack()
        s.push(5)
        s.empty()
        print(s.pop(),'------')
        print(s.isEmpty())
        print(s.isFull())
        s.push(5)
        s.push(8)
        s.push('a')
        print(s.pop())
        s.push('b')
        s.push('c')
        s.show()
        s.showRemainderSpace()
        s.setSize(3)
        print(s.isFull())
        s.show()
        s.setSize(5)
        s.push('d')
        s.push('dddd')
        s.push(3)
        s.show()
        print('Please use me as a module.')

