f = open('test.txt') #打开文件
me = []
you = []
count = 1
for each_line in f:   #遍历文件中的每一行    
    if each_line[:6] != '======': #如果该行的前6个字符不等于======的话
        (role, line_spoken) = each_line.split(':',1)#就将改行以：分割一次，分成的两部分分别存入role, line_spoken两个变量中
        if role == '我': #如果该行的：前面部分是'我'的话，就将该行后面部分追加到me列表中
            me.append(line_spoken)
        if role == '你': #如果该行的：前面部分是'你'的话，就将该行后面部分追加到you列表中
            you.append(line_spoken)
    else:#如果该行的前6个字符等于======的话,那么就将me和you中的元素写入对应的文件中
        file_name_me = 'me_' + str(count) + '.txt'   #定义两个文件名
        file_name_you = 'you_' + str(count) + '.txt'

        me_file = open(file_name_me,'w')   #以写的方式打开文件，不存在则新建一个：当前目录
        you_file = open(file_name_you,'w')

        me_file.writelines(me) #将me中的元素以行的方式，一行一行的写进me_file
        you_file.writelines(you)#将you中的元素以行的方式，一行一行的写进you_file

        me_file.close()  #完事关闭打开的文件
        you_file.close()

        me = []#清空该段对话，以保存下一段对话的数据
        you = []
        count += 1  #文件命名用的加1
        
file_name_me = 'me_' + str(count) + '.txt'
file_name_you = 'you_' + str(count) + '.txt'

me_file = open(file_name_me,'w')
you_file = open(file_name_you,'w')

me_file.writelines(me)
you_file.writelines(you)

me_file.close()
you_file.close()
me = []#清空该段对话，以保存下一段对话的数据
you = []

f.close()
