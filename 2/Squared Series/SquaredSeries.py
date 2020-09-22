def power2 (number):    
    counter = 0
    result = 1
    result_final = [0]
    while result < number :        
        counter += 1
        result_final.append(counter)
        result *= 2
    return result_final
        
def main():
    # [(0, 1), (1, 2), (2, 4), (3, 8), (4, 16), (5, 32), (6, 64), (7, 128), (8, 256), (9, 512), (10, 1024)]
    number = int(input())
    powers_and_numbers = power2(number)
    result = [] 
    result_sum = 0
    last_sum = 0
    for i in range(-1, -1*len(powers_and_numbers)-1, -1) :       
        sum = 2 ** powers_and_numbers[i]
        if result_sum < number : 
            result.insert(0, str(powers_and_numbers[i])) ; result_sum += sum            
        elif result_sum > number :
            result_sum -= last_sum ; del result[0]
            result.insert(0, str(powers_and_numbers[i])) ; result_sum += sum
        else : return result
        last_sum = sum
    return result

print(" ".join(main()))