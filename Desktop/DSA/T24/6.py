# Sum of numbers in the given range

def sum_of_a_given_range(start,end):
    
    total_sum=0
    
    for num in range(start,end+1):
        
        total_sum += num
        
    return total_sum

print(sum_of_a_given_range(1, 10))