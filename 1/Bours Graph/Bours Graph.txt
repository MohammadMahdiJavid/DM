
def counterhorof(vorodi):    
    rc = 0; fc = 0; cc = 0
    for i in vorodi:
        if(i == "F"):
            fc += 1
        elif(i == "R"):
            rc += 1
        else:
            cc += 1
    return rc, fc, cc
def draw(result):
    for i in range(len(result)):
        for j in result[i]:
            print(j, end="")
        if(i!=len(result)-1):
            print()
def first(result, row):
    for i in range (0, row):
        result.append(list())
def second(result, vorodi):
    for i in range(len(vorodi)+3):
        if(i==0):
            result[len(result)-1].append('+')
        else:
            result[len(result)-1].append('-')
def third(result, vorodi):
    for i in range(len(result)-1):
        result[i].append("|"); result[i].append(" ")
def porkardan(result, row):
    for i in range(len(result)):
        if(i==row) or (i==len(result)-1):
            continue
        else:
            result[i].append(" ")
def l_khali(coloumn):
    result=list()
    for i in range(coloumn+1):
        if(i==0):
            result.append("|")
        else:
            result.append(" ")
    return result
def next_move(first, second, row):
    if(first=="R" and second=="R")or(first=="R" and second=="C"):
        return row-1
    elif(first=="C" and second=="F")or(first=="F" and second=="F"):
        return row+1
    elif(first=="R" and second=="F")or(first=="C" and second=="R")or(first=="C" and second=="C")or(first=="F" and second=="C")or(first=="F" and second=="R"):
        return row
def pilot(result, vorodi):
    l_vorodi = list(vorodi); row = len(result)-2; coloumn = 2
    for i in range(len(l_vorodi)):
        if(row==-1):
            result.insert(0, l_khali(coloumn-1)); row+=1
        if(row==len(result)-1):
            result.insert(len(result)-1, l_khali(coloumn-1)); 
        if(l_vorodi[i]=="R"):
            result[row].append("/")
            porkardan(result, row)
            if(i!=len(l_vorodi)-1):
                row = next_move(l_vorodi[i], l_vorodi[i+1], row); coloumn+=1
        elif(l_vorodi[i]=="C"):
            result[row].append("_")
            porkardan(result, row)
            if(i!=len(l_vorodi)-1):
                row = next_move(l_vorodi[i], l_vorodi[i+1], row); coloumn+=1
        elif(l_vorodi[i]=="F"):
            result[row].append("\\")
            porkardan(result, row)
            if(i!=len(l_vorodi)-1):
                row = next_move(l_vorodi[i], l_vorodi[i+1], row); coloumn+=1
def drawlist(vorodi, result):
    row = 2
    first(result, row)
    second(result, vorodi)
    third(result, vorodi)
    pilot(result, vorodi)

def operation():
    vorodi = input()
    result = list()
    drawlist(vorodi, result)
    draw(result)

operation()