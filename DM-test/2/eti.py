def MaximumValue(*params):
    l1 = list(params)
    max_val = l1[0]
    for i in l1:
        if(i>max_val):
            max_val = i
            
print(MaximumValue(1, 2, 3, 4, 5))