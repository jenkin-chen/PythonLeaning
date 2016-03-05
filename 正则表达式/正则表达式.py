import re


print('ok')
re.search(r'fish.','i love fish.com')

re.search(r'\d\d\d','i love 165 .com')

re.search(r'a{1,2}','l aam boy')

re.search(r'[a-z]','wo shi')

re.search(r'(ad){2}','ni wo adg adad')

re.findall(r'\bfishc\b','fishc.com!fishc_com!(fishc)')

p = re.compile(r'A-Z')  #将经常使用的的正则表达式编译成一个模式对象
p.search('I love FISHC.com')

print('ok')
