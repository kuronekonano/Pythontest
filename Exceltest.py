#将多个Excel文件合并成一个
import xlrd
import xlsxwriter
global f8, f9, s84, s85, s94, s95
f8=f9=s84=s85=s94=s95=0
#打开一个excel文件
def open_xls(file):
    fh=xlrd.open_workbook(file)
    return fh

#获取excel中所有的sheet表
def getsheet(fh):
    return fh.sheets()

#获取sheet表的行数
# def getnrows(fh,sheet):
#     table=fh.sheets()[sheet]
#     return table.nrows
def changestart(x,y):
    return int(x/y*100)
#读取文件内容并返回行内容
def getFilect(file,shnum):
    fh=open_xls(file)#第fl个文档 的第shnum个表
    table=fh.sheets()[shnum]#第shnum个表
    num=table.nrows#得到行数
    for row in range(num):#遍历这个表的所有行
        tot=0
        rdata=table.row_values(row)#整行信息
        # print(rdata)
        if type(rdata[8]) == float:
            for star in range(4, 9):
                tot += rdata[star]
            for i in range(4, 9):
                rdata[i] = changestart(rdata[i], tot)
        datavalue.append(rdata)
        if type(rdata[8])==int:
            if rdata[2]>=8.0 and rdata[2]<9.0:
                global s84
                s84+=rdata[5]
                global s85
                s85+=rdata[4]
            if rdata[2]>=9:
                global s94
                s94+=rdata[5]
                global s95
                s95+=rdata[4]
    return datavalue#包含了该表中所有行信息

#获取sheet表的个数
def getshnum(fh):
    x=0
    sh=getsheet(fh)#所有表
    for sheet in sh:
        x+=1
    return x


if __name__=='__main__':
    #定义要合并的excel文件列表
    allxls=['D:\KuroNeko\Desktop\程序语言\python\doubanbook-1.xlsx','D:\KuroNeko\Desktop\程序语言\python\doubanbook-2.xlsx']
    #存储所有读取的结果
    datavalue=[]
    for fl in allxls:
        fh=open_xls(fl)#读入文档
        x=getshnum(fh)#统计表个数
        for shnum in range(x):
            print("正在读取文件："+str(fl)+"的第"+str(shnum)+"个sheet表的内容...")
            rvalue=getFilect(fl,shnum)#读入表内容
    #定义最终合并后生成的新文件
    endfile='D:\KuroNeko\Desktop\程序语言\python\\result_excel.xlsx'
    wb1=xlsxwriter.Workbook(endfile)# 建立合并结果文件
    #创建一个sheet工作对象
    ws=wb1.add_worksheet()#建表
    for a in range(len(rvalue)):  #遍历读入完所有文档所有表的列表，其中a为很多行，b为每行的内容
        for b in range(len(rvalue[a])):
            c=rvalue[a][b]
            if(b==2 and type(c)!=str):
                if c>=8 and c<9:f8+=1
                if c>=9:f9+=1
            ws.write(a,b,c)#表的a行b列写入内容c
    wb1.close()
    print("文件合并完成")
    print('8分以上书籍数目：',f8)
    print('9分以上书籍数目：',f9)
    print('8分组四星评价平均值：%.2f%%'%(s84/f8))
    print('8分组五星评价平均值：%.2f%%'%(s85/f8))
    print('9分组四星评价平均值：%.2f%%'%(s94/f9))
    print('9分组五星评价平均值：%.2f%%'%(s95/f9))