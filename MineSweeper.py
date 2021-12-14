import random
import sys
import time 
import os
from getpass import getpass

def loadingAnimation():
    animation = "|/-\\"

    for i in range(100):
        time.sleep(0.1)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    print ("End!")
def clearConsole():
    os.system('clear')
def progress(count, total, status=''):
    bar_len = 20
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()
def makeMap(mapSize):
    num = 0
    global ll
    ll = []
    if mapSize == 9 or mapSize == 12:
        firstStart = 1
        SecondFinish = mapSize+1
        for i in range(mapSize):
            ll.append(["| {} |".format(i) for i in range(firstStart+100,SecondFinish+100)])
            SecondFinish = SecondFinish + mapSize
            firstStart = SecondFinish - mapSize
        return ll
    elif mapSize == 15:
        firstStart = 1
        SecondFinish = mapSize+1
        for i in range(20):
            ll.append(["| {} |".format(i) for i in range(firstStart+100,SecondFinish+100)])
            SecondFinish = SecondFinish + mapSize
            firstStart = SecondFinish - mapSize
        return ll
    else:
        return "Map not found!"
def mapShow(mapSize):
    if mapSize == 9 or mapSize == 12 or mapSize == 15:
        ll = makeMap(mapSize)
        for i in ll:
            if i == ll[-1]:
                print('--------'*(mapSize))
                print(*i)
                print('--------'*(mapSize))
            else:
                print('--------'*(mapSize))
                print(*i)
        return '***********\nPlease type your choice...'
    else:
        print('Map not found! try again')
def bombPutter(mapSize):
    bombList = []
    if mapSize == 9:
        list1 = [101 ,110 ,119 ,128 ,137 ,146 ,155 ,164 ,173 ]
        list2 = [i+1 for i in list1]      
        list3 = [i+1 for i in list2]
        list4 = [i+1 for i in list3]
        list5 = [i+1 for i in list4]
        list6 = [i+1 for i in list5]
        list7 = [i+1 for i in list6]
        list8 = [i+1 for i in list7]
        list9 = [i+1 for i in list8]
        while len(bombList) < 10:
            selectedList = random.choice([list1,list2,list3,list4,list5,list6,list7,list8,list9])
            rep = random.randint(1,3)
            for i in range(rep):
                selectItem = random.randint(0,8)
                selectedItem = selectedList[selectItem]
                if selectedItem not in bombList:
                    bombList.append(selectedItem)
                else:
                    continue
                if len(bombList) == 10:
                    break
            if len(bombList) == 10:
                break
        return bombList
    elif mapSize == 12:
        list1 = [101 ,113 ,125 ,137 ,149 ,161 ,173 ,185 ,197 ,209 ,221 ,233]
        list2 = [i+1 for i in list1]      
        list3 = [i+1 for i in list2]
        list4 = [i+1 for i in list3]
        list5 = [i+1 for i in list4]
        list6 = [i+1 for i in list5]
        list7 = [i+1 for i in list6]
        list8 = [i+1 for i in list7]
        list9 = [i+1 for i in list8]
        list10 = [i+1 for i in list9]
        list11 = [i+1 for i in list10]
        list12 = [i+1 for i in list11]
        while len(bombList) < 20:
            selectedList = random.choice([list1,list2,list3,list4,list5,list6,list7,list8,list9,list10,list11,list12])
            rep = random.randint(1,3)
            for i in range(rep):
                selectItem = random.randint(0,11)
                selectedItem = selectedList[selectItem]
                if selectedItem not in bombList:
                    bombList.append(selectedItem)
                else:
                    continue
                if len(bombList) == 20:
                    break
            if len(bombList) == 20:
                break
        return bombList
    elif mapSize == 15:
        list1 = [101 ,116 ,131 ,146 ,161 ,176 ,191 ,206 ,221 ,236 ,251 ,266 ,281 ,296 ,311 ,326 ,341 ,356 ,371 ,386 ]
        list2 = [i+1 for i in list1]      
        list3 = [i+1 for i in list2]
        list4 = [i+1 for i in list3]
        list5 = [i+1 for i in list4]
        list6 = [i+1 for i in list5]
        list7 = [i+1 for i in list6]
        list8 = [i+1 for i in list7]
        list9 = [i+1 for i in list8]
        list10 = [i+1 for i in list9]
        list11 = [i+1 for i in list10]
        list12 = [i+1 for i in list11]
        list13 = [i+1 for i in list12]
        list14 = [i+1 for i in list13]
        list15 = [i+1 for i in list14]
        list16 = [i+1 for i in list15]
        list17 = [i+1 for i in list16]
        list18 = [i+1 for i in list17]
        list19 = [i+1 for i in list18]
        list20 = [i+1 for i in list19]
        while len(bombList) < 40:
            selectedList = random.choice([list1,list2,list3,list4,list5,list6,list7,list8,list9,list10,list11,list12,list13,list14,list15,list16,list17,list18,list19,list20])
            rep = random.randint(1,3)
            for i in range(rep):
                selectItem = random.randint(0,19)
                selectedItem = selectedList[selectItem]
                if selectedItem not in bombList:
                    bombList.append(selectedItem)
                else:
                    continue
                if len(bombList) == 40:
                    break
            if len(bombList) == 40:
                break
        return bombList
def makeMapByList(madeMapList,mapSize):
    for i in madeMapList:
        if i == madeMapList[-1]:
            print('--------'*(mapSize))
            print(*i)
            print('--------'*(mapSize))
        else:
            print('--------'*(mapSize))
            print(*i)
    return '***********\nPlease type your choice...'
def playgame():
    clearConsole()
    print('Welcome to the game, please select one these maps to play:\n1- Small (type s)\n2- Medium (type m)\n3- Large (type l)')
    while 'IM ALIVE': 
        mapSizeStr = input()
        if mapSizeStr == 's':
            mapSize = 9
            break
        elif mapSizeStr == 'm':
            mapSize = 12
            break
        elif mapSizeStr == 'l':
            mapSize = 15
            break
        else:
            print('No valid input, try again')
    if mapSize == 9:
        tedadKolParchamHa = 10
    elif mapSize == 12:
        tedadKolParchamHa = 20
    else:
        tedadKolParchamHa = 40
    print('\t\t*\/ Tedad parcham haye shoma: {} *\/'.format(tedadKolParchamHa))
    print(mapShow(mapSize))
    bombs = bombPutter(mapSize)
    print(bombs)
    myMap = makeMap(mapSize)
    nium = 0
    numberOfFoundedBombs = 0
    kams = 0
    foundedBombs = []
    while 'IM ALIVE':
        userChoiceInput = input().split()
        if userChoiceInput[0].isdigit():
            if (int(userChoiceInput[0]) in bombs) and userChoiceInput[1] == 'L':
                print('You Lost!')
                break
            elif ((int(userChoiceInput[0]) in bombs) or (int(userChoiceInput[0]) not in bombs)) and userChoiceInput[1] == 'R':
                print('| '+userChoiceInput[0]+' |')
                # print(makeMap(mapSize))
                for i in myMap:
                    for j in i:
                        if j == '| '+userChoiceInput[0]+' |':
                            if nium == 0:
                                makeMap(mapSize)
                                nium+=1
                            else:
                                makeMapByList(ll,mapSize)
                            ll[myMap.index(i)][i.index(j)] = '|  \u2690  |'
                            tedadKolParchamHa-=1
                            clearConsole()
                            print('\t\t*\/ Tedaded parcham haye baghi mande: {} *\/'.format(tedadKolParchamHa))

                            numberOfFoundedBombs+=1
                            foundedBombs.append(int(userChoiceInput[0]))
                            if len(bombs) == numberOfFoundedBombs:
                                if set(bombs) == set(foundedBombs):
                                    print('YOU WON!')
                                    kams = 1
                                    break
                                
                                else:
                                    print('Your flags finished and you LOST!')
                                    kams = 1
                                    break
                            else:
                                print(makeMapByList(ll,mapSize))
                    if kams == 1:
                        break
                if kams == 1:
                    break
            elif (int(userChoiceInput[0]) not in bombs) and userChoiceInput[1] == 'L':
                clearConsole()
                numBomb = 0
                NUM = int(userChoiceInput[0])
                if nium == 0:
                    makeMap(mapSize)
                    nium+=1
                else:
                    makeMapByList(ll,mapSize)
                if mapSize == 9:
                    if NUM in [102,103,104,105,106,107,108]:
                        clearConsole()
                        bombCounter = [NUM+1,NUM-1,NUM+mapSize,NUM+mapSize+1,NUM+mapSize-1]
                        for bomb in bombCounter:
                            if bomb in bombs:
                                numBomb+=1
                        for i in myMap:
                            for j in i:
                                if j == '| '+str(NUM)+' |':
                                    ll[myMap.index(i)][i.index(j)] = '| ({}) |'.format(numBomb)
                                    print(makeMapByList(ll,mapSize))            
                    elif NUM in [174,175,176,177,178,179,180]:
                        clearConsole()
                        bombCounter = [NUM+1,NUM-1,NUM-mapSize,NUM-mapSize-1,NUM-mapSize+1]
                        for bomb in bombCounter:
                            if bomb in bombs:
                                numBomb+=1
                        for i in myMap:
                            for j in i:
                                if j == '| '+str(NUM)+' |':
                                    ll[myMap.index(i)][i.index(j)] = '| ({}) |'.format(numBomb)
                                    print(makeMapByList(ll,mapSize))
                    elif NUM in [110,119,128,137,146,155,164]:
                        clearConsole()
                        bombCounter = [NUM+1,NUM+mapSize,NUM-mapSize,NUM+mapSize+1,NUM-mapSize+1]
                        for bomb in bombCounter:
                            if bomb in bombs:
                                numBomb+=1
                        for i in myMap:
                            for j in i:
                                if j == '| '+str(NUM)+' |':
                                    ll[myMap.index(i)][i.index(j)] = '| ({}) |'.format(numBomb)
                                    print(makeMapByList(ll,mapSize))           
                    elif NUM in [118,127,136,145,154,163,172]:
                        clearConsole()
                        bombCounter = [NUM-1,NUM+mapSize,NUM-mapSize,NUM-mapSize-1,NUM+mapSize-1]
                        for bomb in bombCounter:
                            if bomb in bombs:
                                numBomb+=1
                        for i in myMap:
                            for j in i:
                                if j == '| '+str(NUM)+' |':
                                    ll[myMap.index(i)][i.index(j)] = '| ({}) |'.format(numBomb)
                                    print(makeMapByList(ll,mapSize))            
                    elif NUM is 101:
                        clearConsole()
                        bombCounter = [NUM+1,NUM+mapSize,NUM+mapSize+1]
                        for bomb in bombCounter:
                            if bomb in bombs:
                                numBomb+=1
                        for i in myMap:
                            for j in i:
                                if j == '| '+str(NUM)+' |':
                                    ll[myMap.index(i)][i.index(j)] = '| ({}) |'.format(numBomb)
                                    print(makeMapByList(ll,mapSize))            
                    elif NUM is 109:
                        clearConsole()
                        bombCounter = [NUM-1,NUM+mapSize,NUM+mapSize-1]
                        for bomb in bombCounter:
                            if bomb in bombs:
                                numBomb+=1
                        for i in myMap:
                            for j in i:
                                if j == '| '+str(NUM)+' |':
                                    ll[myMap.index(i)][i.index(j)] = '| ({}) |'.format(numBomb)
                                    print(makeMapByList(ll,mapSize))
                    elif NUM is 173:
                        clearConsole()
                        bombCounter = [NUM+1,NUM-mapSize,NUM-mapSize+1]
                        for bomb in bombCounter:
                            if bomb in bombs:
                                numBomb+=1
                        for i in myMap:
                            for j in i:
                                if j == '| '+str(NUM)+' |':
                                    ll[myMap.index(i)][i.index(j)] = '| ({}) |'.format(numBomb)
                                    print(makeMapByList(ll,mapSize))            
                    elif NUM is 181:
                        clearConsole()
                        bombCounter = [NUM-1,NUM-mapSize,NUM-mapSize-1]
                        for bomb in bombCounter:
                            if bomb in bombs:
                                numBomb+=1
                        for i in myMap:
                            for j in i:
                                if j == '| '+str(NUM)+' |':
                                    ll[myMap.index(i)][i.index(j)] = '| ({}) |'.format(numBomb)
                                    print(makeMapByList(ll,mapSize))
                    else:
                        clearConsole()
                        bombCounter = [NUM+1,NUM-1,NUM+mapSize,NUM-mapSize,NUM+mapSize+1,NUM-mapSize-1,NUM+mapSize-1,NUM-mapSize+1]
                        for bomb in bombCounter:
                            if bomb in bombs:
                                numBomb+=1
                        for i in myMap:
                            for j in i:
                                if j == '| '+str(NUM)+' |':
                                    ll[myMap.index(i)][i.index(j)] = '| ({}) |'.format(numBomb)
                                    print(makeMapByList(ll,mapSize))
                elif mapSize == 12:
                    if NUM in [102, 103, 104, 105, 106, 107, 108, 109, 110, 111,]:
                        clearConsole()
                        bombCounter = [NUM+1,NUM-1,NUM+mapSize,NUM+mapSize+1,NUM+mapSize-1]
                        for bomb in bombCounter:
                            if bomb in bombs:
                                numBomb+=1
                        for i in myMap:
                            for j in i:
                                if j == '| '+str(NUM)+' |':
                                    ll[myMap.index(i)][i.index(j)] = '|  {}  |'.format(numBomb)
                                    print(makeMapByList(ll,mapSize))            
                    elif NUM in [234, 235, 236, 237, 238, 239, 240, 241, 242, 243 ]:
                        clearConsole()
                        bombCounter = [NUM+1,NUM-1,NUM-mapSize,NUM-mapSize-1,NUM-mapSize+1]
                        for bomb in bombCounter:
                            if bomb in bombs:
                                numBomb+=1
                        for i in myMap:
                            for j in i:
                                if j == '| '+str(NUM)+' |':
                                    ll[myMap.index(i)][i.index(j)] = '|  {}  |'.format(numBomb)
                                    print(makeMapByList(ll,mapSize))
                    elif NUM in [113, 125, 137, 149, 161, 173, 185, 197, 209, 221]:
                        clearConsole()
                        bombCounter = [NUM+1,NUM+mapSize,NUM-mapSize,NUM+mapSize+1,NUM-mapSize+1]
                        for bomb in bombCounter:
                            if bomb in bombs:
                                numBomb+=1
                        for i in myMap:
                            for j in i:
                                if j == '| '+str(NUM)+' |':
                                    ll[myMap.index(i)][i.index(j)] = '|  {}  |'.format(numBomb)
                                    print(makeMapByList(ll,mapSize))           
                    elif NUM in [124,136,148,160,172,184,196,208,220,232]:
                        clearConsole()
                        bombCounter = [NUM-1,NUM+mapSize,NUM-mapSize,NUM-mapSize-1,NUM+mapSize-1]
                        for bomb in bombCounter:
                            if bomb in bombs:
                                numBomb+=1
                        for i in myMap:
                            for j in i:
                                if j == '| '+str(NUM)+' |':
                                    ll[myMap.index(i)][i.index(j)] = '|  {}  |'.format(numBomb)
                                    print(makeMapByList(ll,mapSize))            
                    elif NUM is 101:
                        clearConsole()
                        bombCounter = [NUM+1,NUM+mapSize,NUM+mapSize+1]
                        for bomb in bombCounter:
                            if bomb in bombs:
                                numBomb+=1
                        for i in myMap:
                            for j in i:
                                if j == '| '+str(NUM)+' |':
                                    ll[myMap.index(i)][i.index(j)] = '|  {}  |'.format(numBomb)
                                    print(makeMapByList(ll,mapSize))            
                    elif NUM is 112:
                        clearConsole()
                        bombCounter = [NUM-1,NUM+mapSize,NUM+mapSize-1]
                        for bomb in bombCounter:
                            if bomb in bombs:
                                numBomb+=1
                        for i in myMap:
                            for j in i:
                                if j == '| '+str(NUM)+' |':
                                    ll[myMap.index(i)][i.index(j)] = '|  {}  |'.format(numBomb)
                                    print(makeMapByList(ll,mapSize))
                    elif NUM is 233:
                        clearConsole()
                        bombCounter = [NUM+1,NUM-mapSize,NUM-mapSize+1]
                        for bomb in bombCounter:
                            if bomb in bombs:
                                numBomb+=1
                        for i in myMap:
                            for j in i:
                                if j == '| '+str(NUM)+' |':
                                    ll[myMap.index(i)][i.index(j)] = '|  {}  |'.format(numBomb)
                                    print(makeMapByList(ll,mapSize))            
                    elif NUM is 244:
                        clearConsole()
                        bombCounter = [NUM-1,NUM-mapSize,NUM-mapSize-1]
                        for bomb in bombCounter:
                            if bomb in bombs:
                                numBomb+=1
                        for i in myMap:
                            for j in i:
                                if j == '| '+str(NUM)+' |':
                                    ll[myMap.index(i)][i.index(j)] = '|  {}  |'.format(numBomb)
                                    print(makeMapByList(ll,mapSize))
                    else:
                        clearConsole()
                        bombCounter = [NUM+1,NUM-1,NUM+mapSize,NUM-mapSize,NUM+mapSize+1,NUM-mapSize-1,NUM+mapSize-1,NUM-mapSize+1]
                        for bomb in bombCounter:
                            if bomb in bombs:
                                numBomb+=1
                        for i in myMap:
                            for j in i:
                                if j == '| '+str(NUM)+' |':
                                    ll[myMap.index(i)][i.index(j)] = '|  {}  |'.format(numBomb)
                                    print(makeMapByList(ll,mapSize))               
                else:
                    if NUM in [102,103,104,105,106,107,108,109,110,111,112,113,114]:
                        clearConsole()
                        bombCounter = [NUM+1,NUM-1,NUM+mapSize,NUM+mapSize+1,NUM+mapSize-1]
                        for bomb in bombCounter:
                            if bomb in bombs:
                                numBomb+=1
                        for i in myMap:
                            for j in i:
                                if j == '| '+str(NUM)+' |':
                                    ll[myMap.index(i)][i.index(j)] = '|  {}  |'.format(numBomb)
                                    print(makeMapByList(ll,mapSize))            
                    elif NUM in [387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399 ]:
                        clearConsole()
                        bombCounter = [NUM+1,NUM-1,NUM-mapSize,NUM-mapSize-1,NUM-mapSize+1]
                        for bomb in bombCounter:
                            if bomb in bombs:
                                numBomb+=1
                        for i in myMap:
                            for j in i:
                                if j == '| '+str(NUM)+' |':
                                    ll[myMap.index(i)][i.index(j)] = '|  {}  |'.format(numBomb)
                                    print(makeMapByList(ll,mapSize))
                    elif NUM in [116, 131, 146, 161, 176, 191, 206, 221, 236, 251, 266, 281, 296, 311, 326, 341, 356, 371, 386 ]:
                        clearConsole()
                        bombCounter = [NUM+1,NUM+mapSize,NUM-mapSize,NUM+mapSize+1,NUM-mapSize+1]
                        for bomb in bombCounter:
                            if bomb in bombs:
                                numBomb+=1
                        for i in myMap:
                            for j in i:
                                if j == '| '+str(NUM)+' |':
                                    ll[myMap.index(i)][i.index(j)] = '|  {}  |'.format(numBomb)
                                    print(makeMapByList(ll,mapSize))           
                    elif NUM in [160,175,190,205,220,235,250,265,280,295,310,325,340,355,370,385]:
                        clearConsole()
                        bombCounter = [NUM-1,NUM+mapSize,NUM-mapSize,NUM-mapSize-1,NUM+mapSize-1]
                        for bomb in bombCounter:
                            if bomb in bombs:
                                numBomb+=1
                        for i in myMap:
                            for j in i:
                                if j == '| '+str(NUM)+' |':
                                    ll[myMap.index(i)][i.index(j)] = '|  {}  |'.format(numBomb)
                                    print(makeMapByList(ll,mapSize))            
                    elif NUM is 101:
                        clearConsole()
                        bombCounter = [NUM+1,NUM+mapSize,NUM+mapSize+1]
                        for bomb in bombCounter:
                            if bomb in bombs:
                                numBomb+=1
                        for i in myMap:
                            for j in i:
                                if j == '| '+str(NUM)+' |':
                                    ll[myMap.index(i)][i.index(j)] = '|  {}  |'.format(numBomb)
                                    print(makeMapByList(ll,mapSize))            
                    elif NUM is 115:
                        clearConsole()
                        bombCounter = [NUM-1,NUM+mapSize,NUM+mapSize-1]
                        for bomb in bombCounter:
                            if bomb in bombs:
                                numBomb+=1
                        for i in myMap:
                            for j in i:
                                if j == '| '+str(NUM)+' |':
                                    ll[myMap.index(i)][i.index(j)] = '|  {}  |'.format(numBomb)
                                    print(makeMapByList(ll,mapSize))
                    elif NUM is 386:
                        clearConsole()
                        bombCounter = [NUM+1,NUM-mapSize,NUM-mapSize+1]
                        for bomb in bombCounter:
                            if bomb in bombs:
                                numBomb+=1
                        for i in myMap:
                            for j in i:
                                if j == '| '+str(NUM)+' |':
                                    ll[myMap.index(i)][i.index(j)] = '|  {}  |'.format(numBomb)
                                    print(makeMapByList(ll,mapSize))            
                    elif NUM is 400:
                        clearConsole()
                        bombCounter = [NUM-1,NUM-mapSize,NUM-mapSize-1]
                        for bomb in bombCounter:
                            if bomb in bombs:
                                numBomb+=1
                        for i in myMap:
                            for j in i:
                                if j == '| '+str(NUM)+' |':
                                    ll[myMap.index(i)][i.index(j)] = '|  {}  |'.format(numBomb)
                                    print(makeMapByList(ll,mapSize))
                    else:
                        clearConsole()
                        bombCounter = [NUM+1,NUM-1,NUM+mapSize,NUM-mapSize,NUM+mapSize+1,NUM-mapSize-1,NUM+mapSize-1,NUM-mapSize+1]
                        for bomb in bombCounter:
                            if bomb in bombs:
                                numBomb+=1
                        for i in myMap:
                            for j in i:
                                if j == '| '+str(NUM)+' |':
                                    ll[myMap.index(i)][i.index(j)] = '|  {}  |'.format(numBomb)
                                    print(makeMapByList(ll,mapSize))
                                    
            else:
                print('no valid input, try again...')
        else:
            print('Your input must be a number and a letter, try again...')
def userLoginAndRegister():
    global flag
    global username
    flag = False
    while "IM ALIVE":
        if flag:
            break
        print("Welcome,\ntype whatever you want:\n1- Register (R)\n2- Login (L)\n3- Back (B)")
        if not os.path.isfile('database.txt'):
            db = open('database.txt','w')
            db.close()
        usChoice = input()
        if usChoice == 'R':
            db = open('database.txt','a+')
            while 1:
                flag = False
                username = input('Please enter your username:\n') 
                password = getpass('Please enter your password:\n')
                if len(username) >= 4 and len(password) >=8:
                    db.write('{}\n'.format(username))
                    db.write('{}\n'.format(password))
                    flag = True
                    clearConsole()
                    break
                else:
                    print('username must more than 4 and password more than 8 characters')
        elif usChoice == 'L':
            flag = False
            db = open('database.txt','r')
            allUsers = db.readlines()
            while flag == False:
                username = input('Please enter your username:\n')
                password = getpass("Please enter your password:\n")
                for k in range(len(allUsers)):
                    if allUsers[k] == '{}\n'.format(username):
                        if (allUsers[k+1] == '{}\n'.format(password)) or (allUsers[k+1] == '{}'.format(password)):
                            flag = True
                            break
        db.close()
        return flag
clearConsole()
userLoginAndRegister()
# Change Name and Play Game
if flag:
    clearConsole()
    print('*** MENU ***')
    print('select, to continue...\n1- Change Name (ch)\n2- Play (p)')
    menuChoice = input()
    if menuChoice == 'ch':
        while 1:
            newName = input('Enter your new name:\n')
            if newName:
                print(username)
                break
        with open('database.txt','r') as myFile:
            lines = myFile.readlines()
            for i in lines:
                if i == '{}'.format(username) or i == '{}\n'.format(username):
                    myIndx = lines.index(i)
                    lines[myIndx] = '{}\n'.format(newName)
                    print('your name has changed!')
                    with open('database.txt','w') as secFile:
                        for k in lines:
                            secFile.write(k)
    elif menuChoice == 'p':
        playgame()
        while 1:
            print("*************")
            print("What do you want to do now?")
            print("*************\n1- Rematch (r)\n2- Exit (e)")
            lastChoice = input()
            if lastChoice == 'e':
                print('Sho khosh!')
                exit()
            elif lastChoice == 'r':
                playgame()





