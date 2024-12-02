
# You are given an array of integers 'ARR' containing N elements. Each integer is in the range [1, N-1], with exactly one element repeated in the array.

# Your task is to find the duplicate element. The duplicate element may be repeated more than twice in the error, but there will be exactly one element that is repeated in the array.

def duplicates_element(array):
    
    freq={}

    for num in array:
        
        if num in freq:
            
            return num
        
        else:
            
            freq[num] = 1
            
    return -1

arr = [1, 3, 4, 2, 2]
print(duplicates_element(arr))