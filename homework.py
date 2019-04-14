import time
import sys
#函数重复次数


def timer(func,*pargs,**kargs):
# func函数名称，后面两个是参数
    start = time.clock()
    # 开始时间
    for i in range(runtime):
        ret = func(*pargs,**kargs)
    elapsed = time.clock() - start
    # 花费时间
    return (elapsed,ret)
    # ret记录最后一次结果


reps=10000
repslist=range(reps)


def forloop():
    res = []
    for x in repslist:
        res.append(abs(x))
    return res
#通过for循环迭代

def listComp():
    return [abs(x) for x in repslist]
#列表解析

def mapCall():
    return list(map(abs,repslist))
#调用map

def genExpr():
    return list(abs(x) for x in repslist)
#生成器表达式

def genFunc():
    def gen():
        for x in repslist:
            yield abs(x)
    return list(gen())
#生成器函数


# ======================================================================
def add(k):
    return k+10

def forloop2():
    res = []
    for x in repslist:
        res.append(add(x))
    return res
#通过for循环迭代

def listComp2():
    return [add(x) for x in repslist]
#列表解析

def mapCall2():
    return list(map(add,repslist))
#调用map

def genExpr2():
    return list(add(x) for x in repslist)
#生成器表达式

def genFunc2():
    def gen():
        for x in repslist:
            yield add(x)
    return list(gen())
#生成器函数


runtime=int(input('输入运行次数：'))
print(sys.version)
for test in (forloop,listComp,mapCall,genExpr,genFunc):
    elapsed, result = timer(test)
    print ('{0:10}: {1:.5f} => [{2:}...{3:}]'.format(test.__name__,elapsed,result[0],result[-1]))
print ('-'*40)
for test in (forloop2,listComp2,mapCall2,genExpr2,genFunc2):
    elapsed, result = timer(test)
    print ('{0:10}: {1:.5f} => [{2:}...{3:}]'.format(test.__name__,elapsed,result[0],result[-1]))