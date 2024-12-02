# Problem statement
# Given an array of integers, find the Kth largest sum subarray For example, given the array [1, -2, 3, -4, 5] and K = 2, the 2nd largest sum subarray would be [3, -4, 5], which has a sum of 4.

# Please note that a subarray is the sequence of consecutive elements of the array.

def  kth_subarray_with_k_sum(array:list[int],k:int)->int:
    
    result=[]
    
    n=len(array)
    for i in range(n):
        
        current  = 0
        
        for j in range(i,n):
            
            current += array[j]
            
            result.append(current)
            
            
    result.sort(reverse=True)
    
    
    if k<=len(result):
        
        return result[k-1]
    
    else:
        
        return -1
    
    
arr = [1, -2, 3, -4, 5]
K = 2
print(kth_subarray_with_k_sum(arr,K))
        