from tkinter import *


def callback():
    var.set('吹牛吧，我不信~')
    

root = Tk()

#定义两个框架
frame1 = Frame(root)
frame2 = Frame(root)


var = StringVar()  #定义一个tkinter的字符串变量，内容可以改
var.set('您所下载的Picture有问题！')
#该textLabel放在frame1框架中，提示文字为：var,并且使可选的
textLabel = Label(frame1,
                  textvariable = var,
                  justify = LEFT,
                  )
textLabel.pack(side = LEFT)

photo = PhotoImage(file = "1.gif")
imagLabel = Label(root,image = photo)
imagLabel.pack(side = RIGHT)

#定义一个button，内容为：‘’，按下后响应函数为callback
theButton = Button(frame2,text = "我已经有18了",command = callback)
theButton.pack()

frame1.pack(padx = 10,pady = 10) #把两个框架的位置设置好
frame2.pack(padx = 10,pady = 10)


mainloop()
