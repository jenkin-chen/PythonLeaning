from tkinter import *

root = Tk()

textLabel = Label(root, text = '您所下载的Picture有问题！') #定义一个Label组件
textLabel.pack()#默认位置

photo = PhotoImage(file = "1.gif") #设置一个图片文件对象

imagLabel = Label(root,image = photo) #将图片
imagLabel.pack()

mainloop()
