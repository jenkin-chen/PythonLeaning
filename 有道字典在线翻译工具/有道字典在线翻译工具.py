import urllib.request
import urllib.parse
import json
from tkinter import *

#url为 POST提交数据的Headers的Request URL:地址（右键审查元素可以获取到post返回的数据）
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=fanyi.logo"
head = {}
data = {}  #存放POST包中的Headers的Form Data

content = input("请输入要翻译的内容：")

data['type'] = 'AUTO'
data['i'] = content   #待翻译内容
data['doctype'] = 'json'
data['xmlVersion'] = '1.8'
data['Keyfrom'] = 'fanyi.web'
data['ue'] = 'UTF-8'
data['action'] = 'FY_BY_CLICKBUTTON'
data['typoResult'] = 'true'

data = urllib.parse.urlencode(data).encode('utf-8')

req = urllib.request.Request(url,data,head) #获取Request对象,add_header追加内容
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36')

response = urllib.request.urlopen(req) #打开Request网页对象
html = response.read().decode('utf-8')

target = json.loads(html)

target = target['translateResult'][0][0]['tgt']

#创建输入框和按钮
root = Tk()
text1 = Text(root)
text1.pack()
text1.insert(END, content)

text2 = Text(root)
text2.pack()

def callback():  #按钮响应事件函数
    text2.insert(END, target)
    
b = Button(root, text="开始翻译", command=callback)
b.pack()
mainloop()
