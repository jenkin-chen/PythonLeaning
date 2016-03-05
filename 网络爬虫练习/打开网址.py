import urllib.request  #导入urllib包中的request模块



url = 'http://www.whatismyip.com.tw'


response = urllib.request.urlopen("http://www.whatismyip.com.tw") #调用所导入的urllib.request模块中urlopen函数打开所要打开的URL地址（网页地址）

html = response.read()  # 读取所打开网页的内容

print(html)#打印该网址的内容，二进制未解码的

html = html.decode("utf-8")#解码该网址的内容，解码方式宣召编码方式来utf-8

print(html)#打印该网址解码后的内容
