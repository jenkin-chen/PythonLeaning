import urllib.request
import urllib.parse
import json

content = input('请输入需要翻译的内容; ')

#打开一个网页，页面上右键审查元素可以在 Network Headers 中找到Request URL: 和 Form Data

#Request URL:
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.baidu.com/link'

#User-Agent  改为一个浏览器的User-Agent，隐藏自己是python程序访问网址的实况，程序伪装自己,这样就不会让网页管理者作为爬虫给静止了
head = {}
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'


#Form Data
data = {}
data['type'] = 'AUTO'
data['i'] = content
data['doctype'] = 'json'
data['xmlVersion'] = '1.8'
data['keyfrom'] = 'fanyi.web'
data['ue'] = 'UTF-8'
data['action'] = 'FY_BY_CLICKBUTTON'
data['typoResult'] = 'true'

data = urllib.parse.urlencode(data).encode('utf-8') #unicode 编码成 utf-8

request = urllib.request.Request(url,data,head) #发起请求，加上自己定义的head来隐藏自己
#也可以在request对象生成之后用add_header函数追加head
#request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')
response = urllib.request.urlopen(request)      #接受响应
#response = urllib.request.urlopen(url,data,head) #加上自己定义的head来隐藏自己，这句可替换上面两句

html = response.read().decode('utf-8') #utf-8 解码成 unicode

#print(html)  #json封装的数据，程序员看的 {"type":"EN2ZH_CN","errorCode":0,"elapsedTime":2,"translateResult":
              #[[{"src":"I love you","tgt":"我爱你"}]],
              #"smartResult":{"type":1,"entries":["","我爱你。"]}}

target = json.loads(html) #用json模块翻译json语句
result = target['translateResult'][0][0]['tgt']

print('翻译结果是： ' + str(result))



