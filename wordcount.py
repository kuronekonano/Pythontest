import os
from collections import Counter
filedir = os.getcwd()+'/txtdir'#获取目标文件夹的路径
filenames=os.listdir(filedir)#获取当前文件夹中的文件名称列表
#先遍历文件名
cnt=Counter()
for filename in filenames:
    filepath = filedir+'/'+filename
    #遍历单个文件，读取行数
    for line in open(filepath):
        a=line.split()
        for str in a:
            for char in str:
                if char in '~!@#$%^&*()_+-"{}[]|?.<>?/=:,;1234567890':
                    break
            else:
                cnt[str]+=1
# cnt=dict(cnt)
for key,value in cnt.items():
    print("{0:20}{1:3}".format(key, value))

#Counter 集成于 dict 类，因此也可以使用字典的方法，
# 此类返回一个以元素为 key 、元素个数为 value 的 Counter 对象集合