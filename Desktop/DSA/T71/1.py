# Problem statement
# Given a sorted array of size N, consisting of only 0’s and 1’s. The problem is to find the position of first ‘1’ in the sorted array Assuming 1 based indexing.

# It could be possible that the array consists of only 0’s or only 1’s. If 1’s are not present in the array then print “-1”.


def findFirstOne(arr, n):
    left = 0
    right = n - 1
    first_one_pos = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == 1:
            # Check if it's the first '1'
            first_one_pos = mid  # Temporarily store position
            right = mid - 1  # Continue searching in the left half
        else:
            left = mid + 1  # Search in the right half
    
    # Return the 1-based index if a '1' was found, otherwise -1
    return first_one_pos + 1 if first_one_pos != -1 else -1

a=[2,3,1,4,5]
print(findFirstOne(a,5))