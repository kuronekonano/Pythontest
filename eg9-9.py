import tkinter
import tkinter.filedialog
import tkinter.colorchooser
import tkinter.messagebox
import tkinter.scrolledtext

app=tkinter.Tk()
app.title('My Notepad---by KuroNeko')
app['width']=800
app['height']=600

textChanged=tkinter.IntVar(value=0)

filename=''

menu=tkinter.Menu(app)

submenu=tkinter.Menu(menu,tearoff=0)
def Open():
    global filename

    if textChanged.get():
        yesno=tkinter.messagebox.askyesno(title='Save or not?',message='Do you want to save?')
        if yesno==tkinter.YES:
            Save()
    filename=tkinter.filedialog.askopenfilename(title='Open file',filetypes=[('Text file','*.txt')])

    if filename:
        txtContent.delete(0.0,tkinter.END)
        fp=open(filename,'r')
        txtContent.insert(tkinter.INSERT,''.join(fp.readlines()))
        fp.close()

        textChanged.set(0)

submenu.add_command(label='Open',command=Open)

def Save():
    global filename
    if not filename:
        SaveAs()
    elif textChanged.get():
        fp=open(filename,'w')
        fp.write(txtContent.get(0.0,tkinter.END))
        fp.close()
        textChanged.get(0)

submenu.add_command(label='Save',command=Save)

def SaveAs():
    global filename

    newfilename=tkinter.filedialog.askopenfilename(title='Save As',initialdir=r'd:\\',initialfile='new.txt')

    if newfilename:
        fp=open(newfilename,'w')
        fp.write(txtContent.get(0.0,tkinter.END))
        fp.close()
        filename=newfilename
        textChanged.set(0)

submenu.add_command(label='Save As',command=SaveAs)

submenu.add_separator()

def Close():
    global filename
    Save()
    txtContent.delete(0.0,tkinter.END)
    filename=''

submenu.add_command(label='Close',command=Close)

menu.add_cascade(label='File',menu=submenu)

submenu=tkinter.Menu(menu,tearoff=0)



def Undo():
    txtContent['undo']=True
    try:
        txtContent.edit_undo()
    except Exception as e:
        pass
submenu.add_command(label='Undo',command=Undo)
def Redo():
    txtContent['undo']=True
    try:
        txtContent.edit_redo()
    except Exception as e:
        pass
submenu.add_command(label='Redo',command=Redo)
submenu.add_separator()

def Copy():
    txtContent.clipboard_clear()
    txtContent.clipboard_append(txtContent.selection_get())
submenu.add_command(label='Copy',command=Copy)
def Cut():
    Copy()
    txtContent.delete(tkinter.SEL_FIRST,tkinter.SEL_LAST)
submenu.add_command(label='Cut',command=Cut)
def Paste():
    try:
        txtContent.insert(tkinter.SEL_FIRST,txtContent.clipboard_ger())
        txtContent.delete(tkinter.SEL_FIRST, tkinter.SEL_LAST)
        return
    except Exception as e:
        pass
    txtContent.insert(tkinter.INSERT,txtContent.clipboard_get())
submenu.add_command(label='Paste',command=Paste)
submenu.add_separator()




def Search():
    textToSearch=tkinter.simpledialog.askstring(title='Search',prompt='What to search?')
    start=txtContent.search(textToSearch,0.0,tkinter.END)
    if start:
        tkinter.messagebox.showinfo(title='Found',message='Ok')

submenu.add_command(label='Search',command=Search)
menu.add_cascade(label='Edit',menu=submenu)

txtContent=tkinter.scrolledtext.ScrolledText(app,wrap=tkinter.WORD)
txtContent.pack(fill=tkinter.BOTH,expand=tkinter.YES)
def KeyPress(event):
    textChanged.set(1)
txtContent.bind('<KeyPress>',KeyPress)

app.mainloop()
