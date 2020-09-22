input_numbers = []
while True :
    input_number = int(input())
    if input_number == -1 : break
    input_numbers.append(input_number)

for input_number in input_numbers:
    result = []
    for i in range (input_number+1, 2*input_number+1) :
        j = (i * input_number) / (i - input_number)
        if j.is_integer() :
            result.append((int(j) , i))

    print(len(result))
    for i, j in result :
        print(f"1/{input_number} = 1/{i} + 1/{j}")