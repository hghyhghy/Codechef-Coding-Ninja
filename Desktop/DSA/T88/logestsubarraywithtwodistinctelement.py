# You are given an array ‘fruits’ of size ‘N’. Your task is to find the longest sub-array in the given array such that the count of distinct numbers in the sub-array is less than or equal to 2.

# The sub-array of an array is a contiguous section. For example, for the given array, {2,3,5,1,4} sub-arrays can be {2,3,5}, {3,5,1,4} and so on.

# For Example:
# Consider ‘fruits’ = [1, 2, 1, 3, 2], the longest subarray following the given condition is [1, 2, 1]. The length of the sub-array is 3.

def longest_subarray_with_two_distinct_element(fruits:list[int])->int:
    
    n=len(fruits)
    max_len=float("-inf")

    for i in range(n):
        
        seen=set()
        
        for j in range(i,n):
            
            seen.add(fruits[j])

            if len(seen) > 2 :
                
                break
            
            max_len = max(max_len,j-i+1)
            
    return max_len

fruits = [1, 2, 1, 3, 2]
print(longest_subarray_with_two_distinct_element(fruits))