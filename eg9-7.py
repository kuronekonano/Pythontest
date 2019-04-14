import tkinter
import tkinter.messagebox
def login():#登陆按钮事件处理函数
    name=entryName.get()#获取用户名
    pwd=entryPwd.get()#获取密码
    if name=='SBLX' and pwd =='123456':
        tkinter.messagebox.showinfo(title='Python tkinter',message='OK')
    else:
        tkinter.messagebox.showerror('Python tkinter',message='Error')
def cancel():
    varName.set('')#清空用户输入的用户名和密码
    varPwd.set('')

root=tkinter.Tk()#root只是个窗口名，随便定义即可
varName=tkinter.StringVar(value='')
varPwd=tkinter.StringVar(value='')
labelName=tkinter.Label(root,text='User Name:',justify=tkinter.RIGHT,width=80)#创建用户名标签
labelName.place(x=10,y=5,width=80,height=20)#将标签放到窗口上

entryName=tkinter.Entry(root,width=80,textvariable=varName)#创建文本框，同时设置关联变量
entryName.place(x=100,y=5,width=80,height=20)#将文本框放到窗口上

labelPwd=tkinter.Label(root,text='User Pwd:',justify=tkinter.RIGHT,width=80)#创建密码标签
labelPwd.place(x=10,y=30,width=80,height=20)#将标签放到窗口上

entryPwd=tkinter.Entry(root,show='*',width=80,textvariable=varPwd)#创建密码文本框
entryPwd.place(x=100,y=30,width=80,height=20)#将文本框放到窗口上

buttonOk=tkinter.Button(root,text='Login',command=login)#创建按钮组件，同时设置按钮时间处理函数
buttonOk.place(x=30,y=70,width=50,height=40)#将按钮放到窗口上

buttonCancel=tkinter.Button(root,text='Cancel',command=cancel)
buttonCancel.place(x=120,y=70,width=50,height=40)
root.mainloop()#启动消息循环
