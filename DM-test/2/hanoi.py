# def TowerOfHanoi(moves , start, end, intermediate): 
#     if(moves == 1):
#         print(f"{start} -> {intermediate}")
#         print(f"{intermediate} -> {end}")
#         return
#     TowerOfHanoi(moves-1, start, intermediate, end)

#     print(f"{start} -> {intermediate}") #1-2
#     print(f"{intermediate} -> {end}")   #2-3

#     print(f"{start} -> {intermediate}") #1-2
#     print(f"{end} -> {intermediate}")   #3-2

#     print({intermediate} -> {start})    #2-1
#     print({intermediate} -> {end})      #2-3

#     print({start} -> {intermediate})    #1-2
#     print({start} -> {intermediate})    #1-2

n=int(input()) 

def  sort_backward(m): 
    print( "C -> B" ) 
    print( "B -> A" ) 
    for  i  in  range( 1 ,m): 
        print( "C -> B" ) 
        sort(i) 
        print( "B -> A" ) 
        sort_backward(i) 

def  sort(n): 
    print( "A -> B" ) 
    print( "B -> C" ) 
    for  i  in  range( 1 ,n): 
        print( "A -> B" ) 
        sort_backward(i) 
        print( "B -> C" ) 
        sort(i) 
sort(n)