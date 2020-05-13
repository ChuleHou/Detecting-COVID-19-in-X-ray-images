import sys
import os
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import font  as tkfont
from tkinter import filedialog
import os

tyut = tkinter.Tk()
tyut.geometry('472x400')
tyut.title('智能胸片分析系统')
tyut.button_font = tkfont.Font(family='Helvetica', size=18, weight="bold")
tyut.chose_button_font = tkfont.Font(family='Helvetica', size=15)
tyut.text_font = tkfont.Font(family='Helvetica', size=14, weight="bold")
tyut.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

filename = PhotoImage(file = "/Users/chulehou/Desktop/tyut/Image/background.png")
background_label = Label(tyut, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

label_title = tkinter.Label(tyut,text="欢迎使用智能胸片分析系统", font = tyut.title_font)
label_title.pack()
label_title.place(x = 107, y = 10)

label_text1 = tkinter.Label(tyut,text="请选择需要检测的文件", font = tyut.text_font)
label_text1.pack()
label_text1.place(x = 142, y = 80)

pathtext = tkinter.StringVar()

entry1 = tkinter.Entry(tyut, textvariable=pathtext, width = 30)
entry1.pack()
entry1.place(x = 30, y = 160)

def gettesting():
    tempdir = filedialog.askdirectory(parent=tyut, title='Please select a directory')
    print(tempdir)
    pathtext.set(tempdir)

button1 = tkinter.Button(tyut,text = "选择", font = tyut.chose_button_font, command=gettesting, width = 10)
button1.pack()
button1.place(x = 320, y= 163)

def starttest():
    chosepath = entry1.get()
    print(chosepath)

    splitpath = os.path.basename(chosepath)
    strpath = str('python load_model.py \
                --images ' + splitpath + ' \
                --model covid19.model')
    print(strpath)
    os.system(strpath)    

button2 = tkinter.Button(tyut,text="开始检测", font = tyut.button_font, command=starttest, height = 2, width = 16)
button2.pack()
button2.place(x = 138, y= 280)

tyut.mainloop()