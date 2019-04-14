import tkinter
import tkinter.messagebox
import tkinter.ttk
root=tkinter.Tk()
root.title('A Program Present By KuroNeko')#窗口标题
root['height']=400#定义窗口大小
root['width']=320

labelName=tkinter.Label(root,text='姓名',justify=tkinter.RIGHT,width=50)#创建姓名标签
labelName.place(x=10,y=5,width=50,height=20)                            #将标签放到窗口上

varName=tkinter.StringVar(value='')                         #与姓名关联的变量，默认值为空
entryName=tkinter.Entry(root,width=120,textvariable=varName)#创建文本框，同时设置关联变量
entryName.place(x=70,y=5,width=50,height=20)

labelGrade=tkinter.Label(root,text='年级:',justify=tkinter.RIGHT,width=50)#创建年级标签
labelGrade.place(x=10,y=40,width=50,height=20)                           #将标签放到窗口上
studentClasses={'1':['1','2','3','4'],    #模拟学生所在年级
                '2':['1','2'],            #字典键为年级
                '3':['1','2','3']}        #字典值为班级
comboGrade=tkinter.ttk.Combobox(root,values=tuple(studentClasses.keys()),width=50)#学生年级组合框
comboGrade.place(x=70,y=40,width=50,height=20)

def comboChange(event):#事件处理函数
    grade=comboGrade.get()
    if grade:          #动态改变组合框可选项
        comboClass["values"]=studentClasses.get(grade)
    else:
        comboClass.set([])
comboGrade.bind('<<ComboboxSelected>>',comboChange) #绑定事件处理函数

labelClass=tkinter.Label(root,text='班级:',justify=tkinter.RIGHT,width=50)
labelClass.place(x=130,y=40,width=50,height=20)
comboClass=tkinter.ttk.Combobox(root,width=50)      #学生班级组合框
comboClass.place(x=190,y=40,width=50,height=20)

labelSex=tkinter.Label(root,text='性别:',justify=tkinter.RIGHT,width=50)
labelSex.place(x=10,y=70,width=50,height=20)

sex=tkinter.IntVar(value=1)                                        #与性别关联的变量，1男;0女，默认为男
radioMan=tkinter.Radiobutton(root,variable=sex,value=1,text='男') #单选钮，男
radioMan.place(x=70,y=70,width=50,height=20)
radioWoman=tkinter.Radiobutton(root,variable=sex,value=0,text='女')#单选按钮，女
radioWoman.place(x=130,y=70,width=70,height=20)

monitor=tkinter.IntVar(value=0)  #与是否班长关联的变量，默认不是班长
checkMonitor=tkinter.Checkbutton(root,text='是否班长?',variable=monitor,onvalue=1,offvalue=0)#选中时变量值为1，未选中时变量值为0
checkMonitor.place(x=20,y=100,width=100,height=20)

def addInformation():            #按钮事件处理函数
    result='Name:'+entryName.get()
    result=result+';Grade:'+comboGrade.get()
    result=result+';Class:'+comboClass.get()
    result=result+';Sex:'+('男' if sex.get() else '女')
    result=result+';Monitor:'+('Yes' if monitor.get() else 'No')
    listboxStudents.insert(0,result)
buttonAdd=tkinter.Button(root,text='添加',width=40,command=addInformation)
buttonAdd.place(x=130,y=100,width=40,height=20)

def deleteSelection():
    selection=listboxStudents.curselection()
    if not selection:
        tkinter.messagebox.showinfo(title='Information',message='无可删除信息')#消息框控件
    else:
        listboxStudents.delete(selection)

buttonDelete=tkinter.Button(root,text='删除',width=100,command=deleteSelection)
buttonDelete.place(x=180,y=100,width=40,height=20)

listboxStudents=tkinter.Listbox(root,width=300)      #创建列表框组件
listboxStudents.place(x=10,y=130,width=300,height=200)
root.mainloop()