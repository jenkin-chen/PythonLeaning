import urllib.request
import os
import re
import random

proxies = []

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}

def get_proxy():
    global data,headers,proxies
    req = urllib.request.Request('http://www.xici.net.co',None,headers)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')     
    p = re.compile(r'''<tr\sclass[^>]*>\s+
                                    <td>.+</td>\s+
                                    <td>(.*)?</td>\s+
                                    <td>(.*)?</td>\s+
                                    <td>(.*)?</td>\s+
                                    <td>(.*)?</td>\s+
                                    <td>(.*)?</td>\s+
                                    <td>(.*)?</td>\s+
                                </tr>''',re.VERBOSE)
    proxy_list = p.findall(html)
    for each_proxy in proxy_list[1:]:
        if each_proxy[4] == 'HTTP':
            proxies.append(each_proxy[0]+':'+each_proxy[1])


def url_open(url):
    global proxies
    proxy = random.choice(proxies)
    proxy_support = urllib.request.ProxyHandler({'http':proxy})
    opener = urllib.request.build_opener(proxy_support)
    opener.addheaders = [('User-Agent',headers['User-Agent'])]
    urllib.request.install_opener(opener)

    try:
        req = urllib.request.Request(url,None,headers)
        response = urllib.request.urlopen(req)
        html = response.read()
    except urllib.error.URLError as e:
        print(e.reason)
    
    #print(html)
    return html


def get_page(url): #从网址中获得图片的网页 http://jandan.net/ooxx/page-1877#comments  看规律：每一个都是1877这个数字不同
    html = url_open(url).decode('utf-8')
    a = html.find('current-comment-page') + 23 #<span class="current-comment-page">[1877]</span>
    b = html.find(']',a)                       #用字符串查找的方式查找1877在html 字符串中出现的前后下标
    print(html[a:b])
    return html[a:b]                           #return 1877


def find_imgs(url):#找到网页后找到该网页中所有的图片
    html = url_open(url).decode('utf-8')
    img_addrs = [] #存储所有图片的原地址 <img src="http://ww3.sinaimg.cn/mw600/4bf31e43jw1f1hihxdsv0j20dw0jn0ut.jpg" style="max-width: 480px; max-height: none;">
    a = html.find('img src=')

    while a != -1:
        b = html.find('.jpg',a,a+255)
        if (b != -1):
            img_addrs.append(html[a+9:b+4])
        else:
            b = a + 9
        a = html.find('img src=',b)

    #for each in img_addrs:
    #   print(each)
    return img_addrs #返回图片网址的列表
    


    
def save_imgs(folder,img_addrs):#保存该网页中的所有图片到folder文件夹中
    for each in img_addrs:
        filename = each.split('/')[-1]
        #print(filename)
        with open(filename,'wb') as f:
            img = url_open(each)
            f.write(img)



def download_mm(folder = 'DownloadPicture',pages = 10):#主函数
    if os.path.exists(folder):
        os.rmdir(folder)
    #input('please input any keys to contiue: ')
    os.mkdir(folder)
    os.chdir(folder)
    url = "http://jandan.net/ooxx/"
    page_num = int(get_page(url))
    print('dddddddddd')

    for i in range(pages):
        page_num -= i
        page_url = url + 'page-' + str(page_num) + '#comments'
        img_addrs = find_imgs(page_url)
        save_imgs(folder,img_addrs)

if __name__ == '__main__':
    get_proxy()
    download_mm()
