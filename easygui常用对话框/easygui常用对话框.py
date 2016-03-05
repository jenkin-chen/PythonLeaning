import easygui as g
import sys
def game1():
    g.msgbox('game1 runing','game1')
def game2():
    g.msgbox('game2 runing','game1')
def game3():
    g.msgbox('game3 runing','game1')

while 1:
    g.msgbox('hello，world','My first game')
    choic = g.choicebox('begin the gun!','game',['game1','game2','game3'])

    #g.msgbox('you have choosed' + str(choic),'result')

    if str(choic) == 'game1':
        game1()
    if str(choic) == 'game2':
        game2()
    if str(choic) == 'game3':
        game3()
    if str(choic) == 'None':
        g.msgbox('you have choosed ' + str(choic),'result')

    goodgame = g.buttonbox('which game do you think is the best one?','choose',('game1','game2','game3'))
    if str(goodgame) == 'game1':
        g.msgbox('you choose the game1 is the best one!')
    if str(goodgame) == 'game2':
        g.msgbox('you choose the game2 is the best one!')
    if str(goodgame) == 'game3':
        g.msgbox('you choose the game3 is the best one!')

    index1 = g.indexbox('indexboxtest','indexibox',('yes','no'))
    if index1 == 0:
        g.msgbox('indexbox choose yes')
    if index1 == 1:
        g.msgbox('indexbox choose no')
        

    a = g.multchoicebox('multchoicebox test','multchoicebox',['game1','game2','game3','game4'])
    if a == None:
        print(a)
        a = ['meiyou']
        print(type(a))
    try:
        b = list(g.multchoicebox('multchoicebox test','multchoicebox',a))
    except:
        g.exceptionbox()
    
    
    if g.ccbox('continue the game?','please choose'):
        pass
    else:
        sys.exit(0)

input('please input any key to continue:')
