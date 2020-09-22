def fibbo (number): # 1, 1, 2, 3, 5, 8, 13, 21
    a = 0
    b = 1
    result = []
    if b == number : return [b]
    while b <= number :
        result.append(b)
        a, b = b, a+b
    return result
    
def operation():
    number = int(input())
    fibbo_numbers = fibbo(number)
    result = []                
    for i in range(-1, -1*len(fibbo_numbers)-1, -1):
        result_sum = sum(result)        
        compare_to = 0 if result_sum == number else 1 if result_sum > number else -1
        if compare_to == 0 : return result[::-1]
        elif compare_to == -1 : result.append(fibbo_numbers[i])
        else :
            del result[-1]
            result.append(fibbo_numbers[i])            
    return result

def main() :
    for number in operation():
        print(number, " ", sep = "", end="")

main()            