

#kadane

def main(array):
    
    total=0
    max_sum=float("-inf")

    for num in array:
        
        total += num
        
        if total > max_sum:
            
            max_sum=total
            
        if total < 0:
            
            total =0
            
            
    return max_sum
ARR = [1, 2, -3, 4, 5]
print(main(ARR))