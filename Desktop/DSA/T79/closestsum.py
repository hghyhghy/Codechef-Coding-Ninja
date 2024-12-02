# Given an array 'ARR'' of 'N' integers and an integer 'target', your task is to find three integers in 'ARR' such that the sum is closest to the target.

# Note
# In the case of two closest sums, print the smallest sum.

import sys

def closest_sum(array:list[int],target:int)->int:
    
    n=len(array)
    maximum = sys.maxsize
    
    for i  in range(n):
        
        for j in range(i+1,n):
            
            for k in range(j+1,n):
                
                closest = array[i]+array[j]+array[k]
                
                if abs(closest -target) < abs(maximum -  target):
                    
                    maximum =  closest
                    
                elif abs(closest - target) == abs(maximum -  target):
                    
                    maximum = min(maximum,closest)
                    
    return maximum

arr = [-1, 2, 1, -4]
target = 1
print(closest_sum(arr,target))