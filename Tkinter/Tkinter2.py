import tkinter as tk

class APP:#定义自己的主界面类
    def __init__(self, master):
        frame = tk.Frame(master)  #定义一个框架，由tk生成
        #frame.pack()              #窗口自动调整位置,默认
        frame.pack(side = tk.LEFT,padx = 10,pady = 10) #将窗口处在左边，并且距离x y边都为10

        #定义一个button hi_there，由tk生成，放在frame窗口中，button的提示文字为 “打招呼”，
        #字体为蓝色，背景色为黑色，点击执行的函数未say_hi函数（最主要的）
        self.hi_there = tk.Button(frame,text = "打招呼",fg = 'blue',bg = 'black',command = self.say_hi)
        self.hi_there.pack() #button自己调整位置

    def say_hi(self):#定义hi_there button的响应执行函数
        print("hello everyone!")





if __name__ == "__main__": #自己的测试程序
    root = tk.Tk()   #主体类

    app = APP(root)  #定义自己的主窗口类传进去tk生成的主体root类

    root.mainloop()  #把控制权交给主界面，这是带界面程序主函数的结尾语句，进入事件循环
