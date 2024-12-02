# You have been given a circular array/list ‘ARR’ containing ‘N’ integers. You have to find out the maximum possible sum of a non-empty subarray of ‘ARR’.

# A circular array is an array/list in which the end of the array connects to the beginning of the array.

# A subarray may only include each element of the fixed buffer of ‘ARR’ at most once. (Formally, for a subarray ‘ARR[i]’, ‘ARR[i+1]’, ..., ‘ARR[j]’, there does not exist ‘i’ <= ‘k1’, ‘k2’ <= ‘j’ with ‘k1’ % ‘N’ = k2 % ‘N’.)

# For Example:

# The ‘ARR’ = [1, 2, -3, -4, 5], the subarray [5, 1, 2] has the maximum possible sum which is 8. This is possible as 5 is connected to 1 because ‘ARR’ is a circular array.

def maximum_size_circular_subarray(array:list[int])->int:
    
    n=len(array)
    maximum=float("-inf")

    for i in range(n):
        
        current  =0
        
        for j in range(i,i+n):
            
            current += array[j%n]

            maximum = max(maximum,current)

            if current < 0:
                
                current =0
                
    return maximum

arr = [1, 2, -3, -4, 5]
print(maximum_size_circular_subarray(arr))