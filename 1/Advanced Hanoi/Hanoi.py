def TowerOfHanoi(moves, start="A", end="C", intermediate="B"):
    if(moves==1):
        print(f"{start} -> {intermediate}")
        print(f"{intermediate} -> {end}")
        return
    TowerOfHanoi(moves-1, start, end, intermediate)
    print(f"{start} -> {intermediate}")
    TowerOfHanoi(moves-1, end, start, intermediate)
    print(f"{intermediate} -> {end}")
    TowerOfHanoi(moves-1, start, end, intermediate)

TowerOfHanoi(int(input()))