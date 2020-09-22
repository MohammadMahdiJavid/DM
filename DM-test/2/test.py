import random

l1 = []
for i in range(25):
    j = random.random()
    if(0<j<0.3):
        l1.append("C")
    elif(j<0.6):
        l1.append("F")
    else:
        l1.append("R")

for i in l1:
    print(i, end="")


