import tkinter
import pymysql
import tkinter.messagebox
import tkinter.ttk
class windows:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title('A Program Present By KuroNeko')  # 窗口标题
        self.root['height'] = 400  # 定义窗口大小
        self.root['width'] = 305
        self.setlabeName()#姓名标签与文本框设定
        self.setGrade()#年级标签与选项设定
        self.setClass()#班级标签与选项设定
        self.setSex()#性别标签与选项设定
        self.setMonitor()#是否班长设定
        self.setSQL()

        self.listboxStudents = tkinter.Listbox(self.root)  # 创建列表框组件
        self.listboxStudents.place(x=10, y=130, width=285, height=200)
        self.checkInformation()

        buttonAdd = tkinter.Button(self.root, text='添加', width=40, command=self.addInformation)
        buttonAdd.place(x=130, y=100, width=40, height=20)

        buttonDelete = tkinter.Button(self.root, text='删除', width=100, command=self.deleteSelection)
        buttonDelete.place(x=180, y=100, width=40, height=20)

        self.root.mainloop()

    def setClass(self):
        self.labelClass = tkinter.Label(self.root, text='班级:', justify=tkinter.RIGHT, width=50)
        self.labelClass.place(x=130, y=40, width=50, height=20)
        self.comboClass = tkinter.ttk.Combobox(self.root, width=50)  # 学生班级组合框
        self.comboClass.place(x=190, y=40, width=50, height=20)

    def setlabeName(self):
        self.labelName = tkinter.Label(self.root, text='姓名', justify=tkinter.RIGHT, width=50)  # 创建姓名标签
        self.labelName.place(x=10, y=5, width=50, height=20)  # 将标签放到窗口上

        self.varName = tkinter.StringVar(value='')  # 与姓名关联的变量，默认值为空
        self.entryName = tkinter.Entry(self.root, width=120, textvariable=self.varName)  # 创建文本框，同时设置关联变量
        self.entryName.place(x=70, y=5, width=50, height=20)

    def setGrade(self):
        self.labelGrade = tkinter.Label(self.root, text='年级:', justify=tkinter.RIGHT, width=50)  # 创建年级标签
        self.labelGrade.place(x=10, y=40, width=50, height=20)  # 将标签放到窗口上
        self.studentClasses = {'1': ['1', '2', '3', '4'],  # 模拟学生所在年级
                               '2': ['1', '2'],            # 字典键为年级
                               '3': ['1', '2', '3']}       # 字典值为班级

        self.comboGrade = tkinter.ttk.Combobox(self.root, values=tuple(self.studentClasses.keys()), width=50)  # 学生年级组合框
        self.comboGrade.place(x=70, y=40, width=50, height=20)

        self.comboGrade.bind('<<ComboboxSelected>>', self.comboChange)  # 绑定事件处理函数

    def setSex(self):
        self.labelSex = tkinter.Label(self.root, text='性别:', justify=tkinter.RIGHT, width=50)
        self.labelSex.place(x=10, y=70, width=50, height=20)
        self.sex = tkinter.IntVar(value=1)  # 与性别关联的变量，1男;0女，默认为男
        radioMan = tkinter.Radiobutton(self.root, variable=self.sex, value=1, text='男')  # 单选钮，男
        radioMan.place(x=70, y=70, width=50, height=20)
        radioWoman = tkinter.Radiobutton(self.root, variable=self.sex, value=0, text='女')  # 单选按钮，女
        radioWoman.place(x=130, y=70, width=70, height=20)

    def setMonitor(self):
        self.monitor = tkinter.IntVar(value=0)  # 与是否班长关联的变量，默认不是班长
        checkMonitor = tkinter.Checkbutton(self.root, text='是否班长?', variable=self.monitor, onvalue=1,offvalue=0)  # 选中时变量值为1，未选中时变量值为0
        checkMonitor.place(x=20, y=100, width=100, height=20)

    def setSQL(self):
        self.stu=pymysql.connect("localhost", "root", "970922", "mytest")
        self.cursor=self.stu.cursor()
        
    def comboChange(self,event):#事件处理函数
        grade=self.comboGrade.get()
        if grade:          #动态改变组合框可选项
            self.comboClass["values"]=self.studentClasses.get(grade)
        else:
            self.comboClass.set([])

    def checkInformation(self):
        self.listboxStudents.delete(0,self.listboxStudents.size())
        sqlSelect="select id,name,grade,class,sex,monitor from stu;"
        self.cursor.execute(sqlSelect)
        stuResult=self.cursor.fetchall()
        for it in stuResult :
            result = '姓名: ' + str(it[1])
            result = result + ' ;年级: ' + str(it[2])
            result = result + ' ;班级: ' + str(it[3])
            result = result + ' ;性别: ' + ('男' if it[4] else '女')
            result = result + ' ;是否班长: ' + ('是' if it[5] else '否')
            result = result + ' ;id= ' + str(it[0]);
            self.listboxStudents.insert(self.listboxStudents.size(), result)
            # print(it)

    def addInformation(self):            #按钮事件处理函数,添加数据
        sqlInsert = "insert into stu (Name, Grade, Class, Sex, Monitor) values (%s,%s,%s,%s,%s);"
        prarm = (self.entryName.get(), self.comboGrade.get(), self.comboClass.get(), self.sex.get(), self.monitor.get())
        try:
            self.cursor.execute(sqlInsert,prarm)
            tkinter.messagebox.showinfo(title='插入结果',message='插入成功!')
            self.stu.commit()
        except:
            tkinter.messagebox.showerror(title='插入结果',message='插入失败!')
            self.stu.rollback()
        self.checkInformation()

    def deleteSelection(self):          #删除数据
        selection=self.listboxStudents.curselection()
        if not selection:
            tkinter.messagebox.showinfo(title='Information',message='未选中信息')#消息框控件
        else:
            id=str(self.listboxStudents.get(selection)).split()[11]
            sqlDelete = "delete from stu where id = " + id
            # print(sqlDelete)
            try:
                self.cursor.execute(sqlDelete)
                self.stu.commit()
                tkinter.messagebox.showinfo(title='删除结果', message='删除成功!')
            except:
                tkinter.messagebox.showerror(title='删除结果', message='删除失败!')
                self.stu.rollback()
            self.checkInformation()
if __name__== '__main__':
    windows()