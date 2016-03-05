import tkinter as tk

app = tk.Tk()   #创建主窗口

app.title("My App")#窗口名字

theLabel = tk.Label(app, text = 'My windows') #一个label的

theLabel.pack() #自动调整该label的位置

app.mainloop() #主事件循环，给交界面框架
 
