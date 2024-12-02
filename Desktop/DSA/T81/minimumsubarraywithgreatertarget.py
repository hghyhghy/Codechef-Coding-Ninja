# Rahul is a programming enthusiast. He is currently learning about arrays/lists. One day his teacher asked him to solve a very difficult problem. The problem was to find the length of the smallest subarray(subarray is a contiguous part of an array/list) in a given array/list ‘ARR’ of size ‘N’ with its sum greater than a given value. If there is no such subarray return 0.

# Example: Given an ‘ARR’: [1, 2, 21, 7, 6, 12] and a number ‘X’: 23. The length of the smallest subarray is 2 as the subarray is [21, 7].

# Note: Here are multiple subarrays whose sum is greater than ‘X’ such as [1, 2, 21] or [7, 6, 12] but we have to choose the minimum length subarray.

def minimum_subarray(array:list[int],target:int)->int:
    
    n=len(array)
    minimum = float("inf")
    
    for i in range(n):
        
        current  = 0
        
        for j in range(i,n):
            
            current += array[j]
            
            if current >target:
                
                minimum =min(minimum,j-i+1)
                
                break
            
    return minimum if minimum != float("inf") else 0

arr = [1, 2, 21, 7, 6, 12]
X = 23

print(minimum_subarray(arr,X))
