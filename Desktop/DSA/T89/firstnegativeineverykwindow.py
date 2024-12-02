# Problem statement
# You have been given an array of integers 'ARR' of size 'N'. You are also provided with a positive integer 'K'.

# Your task is to find the first negative element in every window (contiguous subarray) of length 'K'. If there is no negative element in a window, then print 0 for that window.

# For example:
# For the given array 'ARR' = [5, -3, 2, 3, -4] and 'K' = 2.
# Output = -3 -3 0 -4

# We have four windows of length 2 in 'ARR'
# [5, -3] having -3 as first negative element.
# [-3, 2] having -3 as first negative element.
# [2, 3] having no negative element
# [2, -4] having -4 as first negative element.


def first_negative_in_evebry_k_window(array:list[int],k:int)->list[int]:
    
    n=len(array)
    resutt=[]

    for start in range(n-k+1):
        
        negative=  0

        for end in range(start,start+k):

            if array[end] < negative:
                
                negative = array[end]
                break
                
        resutt.append(negative)

    
    return resutt

arr = [5, -3, 2, 3, -4]
k = 2
n = len(arr)

print(first_negative_in_evebry_k_window(arr,k))