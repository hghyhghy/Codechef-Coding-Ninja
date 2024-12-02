# Find four elements that sum to a given value (4Sum) | Set 2
# Last Updated : 16 Apr, 2024
# Given an array of integers, find anyone combination of four elements in the array whose sum is equal to a given value X.

# Example:

# Input: array = {10, 2, 3, 4, 5, 9, 7, 8}, X = 23
# Output: 3 5 7 8
# Explanation: Sum of output is equal to 23, i.e. 3 + 5 + 7 + 8 = 23.

# Input: array = {1, 2, 3, 4, 5, 9, 7, 8}, X = 16
# Output: 1 3 5 7
# Explanation: Sum of output is equal to 16, i.e. 1 + 3 + 5 + 7 = 16.

def finding_one_common_combinations(array,target):
    
    n=len(array)
    array.sort()

    for i in range(n):
        
        for j in range(i+1,n):
            
            for k in range(j+1,n):
                
                for l in range(k+1,n):
                    
                    temp= array[i]+array[j]+array[k]+array[l]

                    if temp == target:
                        
                        return [array[i],array[j],array[k],array[l]]

                    
                    
    return []

a=[10, 2, 3, 4, 5, 9, 7, 8]
x=23

print(finding_one_common_combinations(a,x))
                        