import tkinter
import tkinter.messagebox
import pymysql
import afterlogin
def login():#登陆按钮事件处理函数
    user = pymysql.connect("localhost", "root", "970922", "mytest")
    cursor = user.cursor()
    name=entryName.get()#获取用户名
    pwd=entryPwd.get()#获取密码
    sqlSelect = "select * from pyuser where user_name=\'"+ name +"\' and password= \'" +pwd+ "\';"
    # print(sqlSelect)
    cursor.execute(sqlSelect)
    res=cursor.fetchall()
    if len(res):
        tkinter.messagebox.showinfo(title='登陆成功',message='OK')
        root.destroy()
        afterlogin.windows()
    else:
        tkinter.messagebox.showerror('登陆失败',message='用户名或密码错误')
def cancel():
    varName.set('')#清空用户输入的用户名和密码
    varPwd.set('')

root=tkinter.Tk()#root只是个窗口名，随便定义即可
root.title("欢迎")

varName=tkinter.StringVar(value='')
varPwd=tkinter.StringVar(value='')
labelName=tkinter.Label(root,text='用户名:',justify=tkinter.RIGHT,width=80)#创建用户名标签
labelName.place(x=10,y=5,width=80,height=20)#将标签放到窗口上
entryName=tkinter.Entry(root,width=80,textvariable=varName)#创建文本框，同时设置关联变量
entryName.place(x=100,y=5,width=80,height=20)#将文本框放到窗口上
labelPwd=tkinter.Label(root,text='密码:',justify=tkinter.RIGHT,width=80)#创建密码标签
labelPwd.place(x=10,y=30,width=80,height=20)#将标签放到窗口上

entryPwd=tkinter.Entry(root,show='*',width=80,textvariable=varPwd)#创建密码文本框
entryPwd.place(x=100,y=30,width=80,height=20)#将文本框放到窗口上

buttonOk=tkinter.Button(root,text='登陆',command=login)#创建按钮组件，同时设置按钮事件处理函数
buttonOk.place(x=30,y=70,width=50,height=40)#将按钮放到窗口上

buttonCancel=tkinter.Button(root,text='清除',command=cancel)
buttonCancel.place(x=120,y=70,width=50,height=40)
root.mainloop()#启动消息循环