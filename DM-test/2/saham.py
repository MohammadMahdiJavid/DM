def countermotevali(vorodi, char):
    counter = 0; i = 0
    if(vorodi[0] == char)or(vorodi[0] == "C"):    
        while(True):
            if(i >= len(vorodi)):
                break
            if(vorodi[i] == "C"):
                i += 1
                continue
            if(vorodi[i] == char):
                counter += 1
            else:
                break
            i += 1 
    return counter

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

def pilot(result, vorodi):
    l_vorodi = list(vorodi); row = len(result)-2; coloumn = 2
    for i in range(len(l_vorodi)):
        if(l_vorodi[i]=="R"):
            result[row].append("/")
            porkardan(result, row)
            try:
                if(i==len(l_vorodi)-1):
                    break
                if(l_vorodi[i+1]=="F"):
                    row -= 1
                    coloumn += 1
                    continue
                assert row>0; row -= 1; coloumn += 1; 
            except:
                result.insert(0, l_khali(coloumn))
                coloumn += 1
        elif(l_vorodi[i]=="C"):
            result[row].append("_")
            porkardan(result, row)
            coloumn += 1
        elif(l_vorodi[i]=="F"):
            row += 1
            if(row==len(result)-1):
                result.insert(len(result)-1, l_khali(coloumn-1))
            result[row].append("\\")
            porkardan(result, row)
            coloumn += 1

def row_changes(row, char1, char2):
    if(char1=="F" and char2=="F"):
        return row+1
    if(char1=="R" and char2=="R") or (char1=="R" and char2=="C"):
        return row-1
    if(char1=="C" and char2=="F"):
        return row+1
    return row

def pilotf(result, vorodi):
    l_vorodi = list(vorodi); row = 0; coloumn = 2
    for i in range(len(l_vorodi)):
        if(row==len(result)-1):
            result.insert(row, l_khali(coloumn-1))
        if(row<0)and((l_vorodi[i]=="R")or(l_vorodi[i]=="C")):
            row+=1
            result.insert(0, l_khali(coloumn-1))
        if(l_vorodi[i]=="F"):
            result[row].append("\\")
            porkardan(result, row)
            try:
                row = row_changes(row, l_vorodi[i], l_vorodi[i+1]); coloumn+=1
            except:
                break
        elif(l_vorodi[i]=="R"):
            result[row].append("/")
            porkardan(result, row)
            try:
                row = row_changes(row, l_vorodi[i], l_vorodi[i+1]); coloumn+=1
            except:
                break                
        elif(l_vorodi[i]=="C"):
            result[row].append("_")
            porkardan(result, row)
            try:
                row = row_changes(row, l_vorodi[i], l_vorodi[i+1]); coloumn+=1
            except:
                break            

def last(result):
    for i in range(len(result)-1):
        result[i].append(" ")

def drawlist(vorodi, result, rc, fc, cc):
    j=1000000000000000; i=10000000000000
    if(vorodi.count("R")>0):
        i = vorodi.index("R")
    if(vorodi.count("F")>0):
        j = vorodi.index("F")
    if(j<i):
        fmotevali = countermotevali(vorodi, "F")
        first(result, fmotevali+1)
        second(result, vorodi)
        third(result, vorodi)
        pilotf(result, vorodi)
        last(result)
    else:
        row = 2
        first(result, row)
        second(result, vorodi) # row1
        third(result, vorodi)
        pilot(result, vorodi)
        last(result)
    return result

def draw(result):
    for i in range(len(result)):
        for j in result[i]:
            print(j, end="")
        if(i!=len(result)-1):
            print()


def operation():
    vorodi = input()
    assert 0<len(vorodi)<31
    result = list()
    rc , fc , cc = counterhorof(vorodi)
    draw(drawlist(vorodi, result, rc, fc, cc)) 

operation()