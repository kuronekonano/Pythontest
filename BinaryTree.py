class BinaryTree:
    def __init__(self,value):#构造函数
        self.__left=None
        self.__right=None
        self.__data=value
    def insertLeftChild(self,value):
        if self.__left:
            print('left child tree already exists.')
        else:
            self.__left=BinaryTree(value)
            return self.__left
    def insertRightChild(self,value):
        if self.__right:
            print('Right child tree already exists.')
        else:
            self.__right=BinaryTree(value)
            return self.__right
    def show(self):
        print(self.__data)
    def preOreder(self):#先序遍历
        print(self.__data)
        if self.__left:
            self.__left.preOrder()
        if self.__right:
            self.__right.preOrder()
    def postOrder(self):#后序遍历
        if self.__left:
            self.__left.postOrder()
        if self.__right:
            self.__right.postOrder()
        print(self.__data)
    def inOrder(self):#中序遍历
        if self.__left:
            self.__left.inOrder()
        print(self.__data)
        if self.__right:
            self.__right.inOrder()
    if __name__=='__main__':
        print('Please use me as module.')

# import BinaryTree
# root=BinaryTree.BinaryTree('root')
# b=root.insertRightChild('B')
# a=root.insertLeftChild('A')
# c=a.insertLeftChild('C')
# d=c.insertRightChild('D')
# e=b.insertRightChild('E')
# f=e.insertLeftChild('F')
# root.inOrder()
# root.postOrder()
# b.inOrder()
