class MyArray:
    '''All the elements in this array must be numbers'''
    __value=[]
    __size=0

    def __IsNumber(self,n):
        if (not isinstance(n,int)) and \
           (not isinstance(n,float)) and \
           (not isinstance(n,complex)):
                return False
        return  True

    def __init__(self,*args):
        if not args:
            self.__value=[]
        else:
            for arg in args:
                if not self.__IsNumber(arg):
                    print('All the elements in this array must be numbers')
                    return
            self.__value=list(args)

    def __add__(self, n):  #数组中每个元素都与数字n相加，或两个数组相加
        if self.__IsNumber(n):
            b=MyArray()
            for v in self.__value:
                b.__value.append(v+n)
            return b
        elif isinstance(n,MyArray):
            if len(n.__value)==len(self.__value):
                c=MyArray()
                for i,j in zip(self.__value,n.__value):
                    c.__value.append(i+j)
                return c
            else:
                print('Lenght not equal')
        else:
            print('Not supported')

    def __sub__(self, n):  #数组中每个元素都与数字n相减，返回新数组
        if not self.__IsNumber(n):
            print('- operating with',type(n),'and number type is not supported.')
            return
        b=MyArray()
        for v in self.__value:
            b.__value.append(v-n)
        return b

    def __mul__(self, n):  #数组中每个元素都与数字n相乘，返回新数组
        if not self.__IsNumber(n):
            print('* operating with',type(n),'and number type is not supported.')
            return
        b = MyArray()
        for v in self.__value:
            b.__value.append(v * n)
        return b

    def __truediv__(self, n): #数组中每个元素都与数字n相除，返回新数组
        if not self.__IsNumber(n):
            print(r'/ operating with',type(n),' and number type is not supported.')
            return
        b=MyArray()
        for v in self.__value:
            b.__value.append(v / n)
        return b

    def __floordiv__(self, n): #数组中每个元素都与数字n整除，返回新数组
        if not isinstance(n,int):
            print(n,' is not an interger')
            return
        b=MyArray()
        for v in self.__value:
            b.__value.append(v//n)
        return b

    def __mod__(self, n): #数组中每个元素都与数字n求余数，返回新数组
        if not self.__IsNumber(n):
            print(r'% operating with',type(n),' and number type is not supported.')
            return
        b = MyArray()
        for v in self.__value:
            b.__value.append(v%n)
        return b

    def __pow__(self,n): #数组中每个元素都与数字n进行幂计算，返回新数组
        if not self.__IsNumber(n):
            print('** operating with',type(n),' and number type is not supported.')
            return
        b = MyArray()
        for v in self.__value:
            b.__value.append(v ** n)
        return b

    def __len__(self):
        return len(self.__value)

    def __repr__(self): #直接使用对象作为语句时调用该函数
        #equivalent to return 'self.__value'
        return repr(self.__value)

    def __str__(self): #使用print()函数输出对象时调用该函数
        return str(self.__value)

    def append(self,v): #追加元素
        if not self.__IsNumber(v):
            print('Only number can be appended.')
            return
        self.__value.append(v)

    def __getitem__(self, index): #获取指定位置的元素值
        if self.__IsNumber(index) and 0<=index<len(self.__value):
            return self.__value[index]
        else:
            print('Index out of range.')

    def __setitem__(self, index, v): #设置指定位置的元素值
        if not self.__IsNumber(v):
            print(v,' is not a number')
        elif (not isinstance(index,int)) or index<0 or index>=len(self.__value):
            print('Index type error or out of range')
        else:
            self.__value[index]=v

    def __contains__(self,v):  #成员测试运算符in
        if v in self.__value:
            return True
        return False

    def dot(self, v):  #模拟向量内积
        if not isinstance(v,MyArray):
            print(v,' must be an instance of MyArray.')
            return
        if len(v)!=len(self.__value):
            print('The size must be equal.')
            return
        b=MyArray()
        for m,n in zip(v.__value,self.__value):
            b.__value.append(m*n)
        return sum(b.__value)

    def __eq__(self, v):  #关系运算符==
        if not isinstance(v,MyArray):
            print(v,' must be an instance of MyArray.')
            return False
        if self.__value==v.__value:
            return True
        return False

    def __lt__(self, v): #关系运算符<
        if not isinstance(v,MyArray):
            print(v,' must be an instance of MyArray.')
            return False
        if self.__value<v.__value:
            return True
        return False

    if __name__=='__main__':
        print('Please use me as a module.')
        from MyArray import MyArray
        x = MyArray(1, 2, 3, 4, 5, 6)
        y = MyArray(6, 5, 4, 3, 2, 1)
        print(len(x))
        print(x + 5)
        print(x * 3)
        print(x.dot(y))
        x.append(7)
        print(x)
        x.dot(y)
        # x[9]=8
        print(x / 2)
        print(x // 2)
        print(x % 3)
        print(x[2])
        print('a' in x)
        print(3 in x)
        print(x < y)
        x = MyArray(1, 2, 3, 4, 5, 6)
        print(x + y)

