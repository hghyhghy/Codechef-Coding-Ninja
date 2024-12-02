# You have been given an array(ARR) of positive integers and an integer X. You have to find the minimum length subarray such that the sum of all of its elements is strictly greater than the given integer X.

# Note:
# A subarray is a contiguous block of elements that can be formed by deleting some (possibly zero) elements from the beginning or the end of the original array. 
# For example :
# If the given array is [1, 2, 3, 4, 5], then [2, 3, 4], [1, 2], [5] are some subarrays while [1, 3], [2, 3, 5] are not.

# If there are multiple subarrays with minimum length, find one which appears earlier in the array (i.e. subarray that starts with lower index).

# If there is no such subarray, print an empty line. in python
def minimum_length(array: list[int], x: int) -> int:
    n = len(array)
    min_length = float("inf")  # Initialize min_length to infinity
    curr_sum = 0
    start = 0
    
    for end in range(n):
        curr_sum += array[end]  # Expand the window by including arr[end]
        
        # Shrink the window from the left as long as the sum is greater than x
        while curr_sum > x:
            min_length = min(min_length, end - start + 1)  # Update the minimum length
            curr_sum -= array[start]  # Remove the element at start
            start += 1  # Move the start pointer to the right
    
    return min_length if min_length != float("inf") else 0

# Example usage
arr = [2, 1, 5, 2, 3, 2]
x = 7
ans = minimum_length(arr, x)
print(ans)  # Expected output: 2
