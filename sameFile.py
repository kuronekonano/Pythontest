import hashlib
import os
from collections import Counter
import time
import datetime

def get_md5_01(file_path):
    md5 = None
    if os.path.isfile(file_path): #防止报错，存在该文件时才读取
        f = open(file_path, 'rb')#二进制模式读取文件
        md5_obj = hashlib.md5() #创建hash对象，md5:(message-Digest Algorithm 5)消息摘要算法,得出一个128位的密文
        md5_obj.update(f.read())#更新哈希对象,以字符串为参数 ，此处为读入的文件内容
        hash_code = md5_obj.hexdigest()#返回摘要，作为十六进制数据字符串值    23eeeb4347bdd26bfc6b7ee9a3b755dd
        f.close()
        md5 = str(hash_code).lower()#计算的md5值变为小写
    return md5

#
# def get_md5_02(file_path):
#     f = open(file_path, 'rb')
#     md5_obj = hashlib.md5()
#     while True:
#         d = f.read(8096)
#         if not d:
#             break
#         md5_obj.update(d)
#     hash_code = md5_obj.hexdigest()
#     f.close()
#     md5 = str(hash_code).lower()
#     return md5

def TimeStampToTime(timestamp):
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S',timeStruct)
def get_FileSize(filePath):
    fsize = os.path.getsize(filePath)#文件大小，字节为单位，转换成兆
    fsize = fsize/float(1024*1024)
    return round(fsize,2)
def get_FileCreateTime(filePath):
    t = os.path.getctime(filePath)
    return TimeStampToTime(t)

if __name__ == "__main__":
    output_list = []
    output_path = os.getcwd()#返回当前工作目录
    print(output_path)
    g = os.walk(output_path)#返回当前目录的路径,文件夹名(目录列表)，文件列表
    for path, dir_list, file_list in g:#遍历顺序以目录树的形式，不断递归到更深层的文件夹内
        print(dir_list,'----->')
        print(file_list)
        for file_name in file_list:
            output_list.append(os.path.join(path, file_name))#输出文件路径和文件名，并将主目录路径和文件列表组合成完整路径，将每个文件组装好的路径放入output列表中
    md5_list = [get_md5_01(i) for i in output_list]#对所有文件求md5值，并存在列表中
    Counter_list = Counter(md5_list)#该函数直接对求得的所有md5值计数，并用字典标记每个md5值的出现次数
    print(Counter_list)
    for i in Counter_list.items():
        # print(type(i),i)#items()返回一个元组，表示dict的 键-值，[0]为键，[1]为值
        if i[1] > 1:#一个计数大于1的md5值说明重复出现
            duplicate_list = [a for a in range(len(md5_list)) if md5_list[a] == i[0]]#遍历所有md5值，符合条件的文件下标存下
            print(i[0])#中奖的md5值
            for j in duplicate_list:#将符合条件的文件信息输出
                # with open('duplicate.log', mode='a+') as f:
                #     f.write(i[0] +'\t' + output_list[j] + '\n')
                print('文件路径',output_list[j])
                print('文件大小',get_FileSize(output_list[j]), 'M')
                print('文件创建时间',get_FileCreateTime(output_list[j]))
                print('文件绝对路径',os.path.abspath(output_list[j]))

