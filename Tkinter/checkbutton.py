from tkinter import *


def nextExample():
    root1 = Tk()
    GIRLS = ['西施','貂蝉','王昭君','杨玉环']

    v = []
    for eachgirl in GIRLS:
        v.append(IntVar())
        b = Checkbutton(root1,text = eachgirl,variable = v[-1])#每次都获得v的最后一个
        b.pack(anchor = W) #Checkbutton顶靠在左边


    #单选框
    v1 = IntVar()
    Radiobutton(root1,text = 'one',variable = v1,value = 1).pack(anchor = W)
    Radiobutton(root1,text = 'two',variable = v1,value = 2).pack(anchor = W)
    Radiobutton(root1,text = 'three',variable = v1,value = 3).pack(anchor = W)

    #mainloop()


root = Tk()
v = IntVar()#定义一个可变的Int变量
myCheckButton = Checkbutton(root,text = 'Test',variable = v) #选中了就为1，未选中就为0
myCheckButton.pack() #默认位置

myLabel = Label(root,textvariable = v) #定义一个Label，Label的文字（可变的text）显示v变量的值，

myLabel.pack() #Label的位置默认

theButton = Button(root,text = "next",command = nextExample)
theButton.pack()


mainloop()#事件循环



