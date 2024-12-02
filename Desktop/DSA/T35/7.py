# Problem statement
# Ninja is given an array ‘Arr’ of size ‘N’. You have to help him find the longest subarray of ‘Arr’, whose sum is 0. You must return the length of the longest subarray whose sum is 0.

def longest_subarry_with_zero_sum(array):
    
    n=len(array)
    lenght=0
    
    for i in range(n):
        
        current_sum = 0
        
        for j in range(i,n):
            
            current_sum += array[j]

            if current_sum == 0:
                
                custom_lenght= j-i+1
                
                lenght = max(lenght,custom_lenght)

    return lenght

arr = [1, 2, -2, 4, -4]

print(longest_subarry_with_zero_sum(arr))