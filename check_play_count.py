import pymysql

db = pymysql.connect("localhost", "root", "970922", "mytest")

cursor = db.cursor()

sqlAvg = "select avg(total_play_count) from user;"#直接调用MYSQL中的平均值查询代码
cursor.execute(sqlAvg)
avgResult = cursor.fetchone()
print("平均播放量：%.2f" % avgResult[0])
print("超过平均播放量的用户信息：")
sqlMoreThanAvg = "select name, password, face_pic_id, last_login_time, visit_count, total_play_count from user where total_play_count >  (select avg(total_play_count) from user);"
cursor.execute(sqlMoreThanAvg)
useResult = cursor.fetchall()
for i in useResult:
    print(i)