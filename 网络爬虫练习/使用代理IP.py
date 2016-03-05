#去网上查询 代理ip,有很多可供使用的代理ip
import urllib.request
import random
import time

url = 'http://www.whatismyip.com.tw'

iplist = ['125.62.14.162:3128','118.26.143.202:3128','14.25.27.84:3128']#这个列表可以编写代码从网上下载代理ip地址

while True:
    userinput = input("Please input q! to exit: ")
    if userinput == 'q!':
        break

    #第一步：去网上查询 找到一个代理ip地址，创建一个代理，参数是一个字典类型{'类型':'代理ip:端口号'}
    proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})

    #第二步：定制、创建一个opener，并且将opener的addheaders 属性更改为一个正常的addheaders 
    opener = urllib.request.build_opener(proxy_support)
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')]

    #第三步：安装opener
    urllib.request.install_opener(opener)


    #第四步：调用opener
    response = urllib.request.urlopen(url) #安装好后，普通调用urlopen函数则是直接调用安装好的opener代理地址进行访问的
     
    html = response.read().decode('utf=8')
    time.sleep(3)#休眠3秒

    print(html)

