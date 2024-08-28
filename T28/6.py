# You are given an array/list of ‘N’ integers. You are supposed to return the maximum sum of the subsequence with the constraint that no two elements are adjacent in the given array/list.

def max_sum_of_adjacent_element(arr):
    
    max_sum = 0
    odd=0
    even=0
    n=len(arr)

    for i in range(0,n):
        
        if i % 2 == 0:
            
            even += arr[i]

        else:
            
            odd += arr[i]
            
        
        
    return  max(even,odd)

        
arr = [3, 2, 5, 10, 7]
print(max_sum_of_adjacent_element(arr))