import random
import sys
import time 
import os

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
                # print('--------'*(mapSize))
                print(*i)
                # print('--------'*(mapSize))
            else:
                # print('--------'*(mapSize))
                print(*i)
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
# clearConsole()
# total = 10
# i = 0
# clearConsole()
# while i <= total:
#     progress(i, total, status='Loading components...')
#     time.sleep(1)  # emulating long-playing job
#     i += 1
# clearConsole()
# n = int(input())
# print(bombPutter(n))
# print(mapShow(n))



