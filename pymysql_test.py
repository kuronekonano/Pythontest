import pymysql
import time

db = pymysql.connect("localhost", "root", "970922", "mytest")#分别为，域名，用户名，密码，库名

cursor = db.cursor()

createTime = time.time()#获取当前时间
local = time.localtime(createTime)#格式化时间戳为本地的时间
loginTime = str(time.strftime('%Y-%m-%d %H:%M:%S', local))#函数接收以时间元组，并返回以可读字符串表示的当地时间，格式由参数format决定。
#将MYSQL插入语句进行字符串式的转换
sqlInsert = "insert into user (name, password, face_pic_id, last_login_time, visit_count, total_play_count) values (%s,%s,%s,%s,%s,%s);"
#sqlInsert2 = "insert into users (name, password, face_pic_id, last_login_time, visit_count, total_play_count) values ('dadong', 'das', 20, 'time', 0, 0);"
#%s为参数
try:
    print("输入用户名：", end="")
    name = input()
    print("输入密码：", end="")
    password = input()
    print("输入face_pic_id：", end="")
    face_pic_id = int(input())
    print("输入浏览量：", end="")
    visitCount = input()
    print("输入播放量：", end="")
    playCount = input()
    prarm = (name, password, face_pic_id, loginTime, visitCount, playCount)#参数
    n = cursor.execute(sqlInsert, prarm)
    # cursor.execute(sqlInsert2)
    print("insert ok!")
    db.commit()
except:
    print("insert error!")
    db.rollback()
sqlSelect = "select name, password, face_pic_id, last_login_time, visit_count, total_play_count from user;"
cursor.execute(sqlSelect)
userResult = cursor.fetchall()
#首先fetchone()函数它的返回值是单个的元组,也就是一行记录,如果没有结果,那就会返回null
#其次是fetchall()函数,它的返回值是多个元组,即返回多个行记录,如果没有结果,返回的是()
for i in userResult:
    print(i)

# print("输入要删除的id：", end=" ")
# id = input()
# sqlDelete = "delete from users where id = " + id
# try:
#     cursor.execute(sqlDelete)
#     print("delete ok!")
#     db.commit()
# except:
#     print("delete error!")
#     db.rollback()

db.close()
