import sqlite3
conn =sqlite3.connect('example.db')
c=conn.cursor()
# c.execute("drop table user")
# c.execute('''
# CREATE TABLE user
# (
#   `id` INTEGER PRIMARY KEY AUTOINCREMENT  ,#用户ID
#   `name` varchar(20) NOT NULL ,#用户姓名
#   `password` varchar(20) NOT NULL,#用户密码
#   `face_pic_id` int(11) NOT NULL,#用户
#   `last_login_time` timestamp NULL DEFAULT '0000-00-00 00:00:00',
#   `visit_count` int(11) NOT NULL ,
#   `total_play_count` int(11) NOT NULL
# );''')#建表
# c.execute("SELECT name FROM sqlite_master WHERE type='table';")
# print(c.fetchall())
# c.execute("INSERT INTO 'user' VALUES (01,'张强民','123456',56,'2018-09-24 08:26:45',156,5489)")
# c.execute("INSERT INTO 'user' VALUES (02,'林一帆','654321',89,'2017-10-11 18:56:56',12,12356)")
# c.execute("INSERT INTO 'user' VALUES (03,'赵琳','147852',77,'2018-08-02 22:35:42',455,72944)")
# c.execute("INSERT INTO 'user' VALUES (04,'李方方','258963',2,'2018-10-31 12:33:34',23,4458)")
# c.execute("INSERT INTO 'user' VALUES (05,'王敏','369852',264,'2018-10-16 04:46:21',77,10024)")
# c.execute("INSERT INTO 'user' VALUES (06,'李明','789456',781,'2018-08-05 23:17:08',104,6663)")
# c.execute("INSERT INTO 'user' VALUES (07,'韦严平','654987',21,'2018-10-21 17:22:02',261,1234)")
conn.commit()
# conn.close()
# c.execute("CONSTRAINT 'user_ibfk_1' FOREIGN KEY ('face_pic_id') REFERENCES 'face'('id') ON DELETE")
print('所有用户列表：')
for row in c.execute('SELECT * FROM user ORDER BY visit_count;'):#查表
    print(row)
visit_sum=sum([i[0] for i in c.execute('SELECT visit_count FROM user')])
visit_avg=visit_sum/len([i[0] for i in c.execute('SELECT visit_count FROM user')])
print('所有用户播放次数平均值：',visit_avg)
print('播放次数超过平均播放量的用户：')
for row in c.execute('SELECT * FROM user'):
    if row[5]>visit_avg:print(row)
    else :pass