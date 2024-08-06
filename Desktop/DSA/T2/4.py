# Given an array of integers, such as [-2, 1, -3, 4, -1, 2, 1, -5, 4], the algorithm should determine that the maximum subarray sum is 6 ([4, -1, 2, 1]).

def maximum_subarray_sum(arr):
    
    max_sum=arr[0]
    n=len(arr)

    for i in range(n):
        
        for j in range(i,n):
            
            total_sum = sum(arr[i:j+1])

            if total_sum > max_sum:
                
                max_sum =  total_sum
                
    return max_sum


p=[-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maximum_subarray_sum(p))