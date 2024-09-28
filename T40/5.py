# Problem statement
# You are given a non-decreasing array and an integer K. You need to remove exactly K integers from the given array such that the maximum difference between adjacent elements is minimum.

# For example:
# If the given array is: [2 6 7 7 10] and K = 2. We need to remove A[0] = 2 and A[4] = 10, then the resultant array would become [6 7 7], where the difference between adjacent pairs are {1, 0}. Thus our answer would be 1. You can see that there would not be any better answer than 1 for this array

def delete_k_elements_from_the_array(array,k):
    
    n=len(array)

    if k >=n:
        
        return array
    
    for i in range(k+1,n+1):
        
        print(array[i-1])
        
    

arr = [1, 3, 5, 7, 9]
K = 2

print(delete_k_elements_from_the_array(arr,K))