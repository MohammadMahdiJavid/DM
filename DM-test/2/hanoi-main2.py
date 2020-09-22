def TowerOfHanoi(moves , one, two, three, four):
    if(moves==1):
        print(f"{one} -> {two}")
        print(f"{three} -> {four}")
    TowerOfHanoi(moves-1, one, two, three, four)
    TowerOfHanoi()

TowerOfHanoi("A", "B", "B", "C")



# print(f"{start} -> {intermediate}") #1-2
# print(f"{intermediate} -> {end}")   #2-3

# print(f"{start} -> {intermediate}") #1-2
# print(f"{end} -> {intermediate}")   #3-2

# print({intermediate} -> {start})    #2-1
# print({intermediate} -> {end})      #2-3

# print({start} -> {intermediate})    #1-2
# print({start} -> {intermediate})    #1-2