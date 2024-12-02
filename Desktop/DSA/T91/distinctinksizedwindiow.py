# Problem statement
# Given an array of integers ‘arr’ of size ‘n’ and an integer ‘k’. You need to find the count of distinct elements in every sub-array of size ‘k’ in the given array. Return an integer array ‘count’ that consists of n - k + 1 integers where ‘count[i]’ is equal to the number of distinct elements in a sub-array of size ‘k’ starting from index ‘i’.

# Note:
# 1. The sub-array of an array is a continuous part of the array.
# 2. Consider ‘0’ based indexing.
# 3. ‘k’ will always be less than or equal to ‘n’.
# 3. Don’t print anything, just return the integer array ‘count’.

def distinct_in_k_sized_window(array:list[int],k:int)->list[int]:
    
    n=len(array)
    result=[]
    
    for i in range(n-k+1):
        
        distinct=set()

        for j in range(i,i+k):
            
            distinct.add(array[j])

        result.append(len(distinct))

    
    return result

arr = [1, 2, 2, 1, 3, 1, 1, 3]
k = 4
print(distinct_in_k_sized_window(arr,k))