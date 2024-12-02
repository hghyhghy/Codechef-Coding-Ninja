# Problem statement
# You are given an unsorted array/list 'ARR' of 'N' integers. Your task is to return the length of the longest consecutive sequence.

# The consecutive sequence is in the form ['NUM', 'NUM' + 1, 'NUM' + 2, ..., 'NUM' + L] where 'NUM' is the starting integer of the sequence and 'L' + 1 is the length of the sequence.

# Note:

# If there are any duplicates in the given array we will count only one of them in the consecutive sequence.

def longest_consecutive_substring(array):
    
    if not array:
        
        return 0
    array.sort()

    max_length=1
    count =1
    n=len(array)

    for i in range(n):
        
        if array[i] == array[i-1]+ 1:
            
            count += 1
            
        elif array[i] == array[i-1]:
            
            continue
        
        else:
            
            max_length = max(max_length,count)
            count = 1
            
            
    max_length = max(max_length,count)

    return max_length

arr = [100, 4, 200, 1, 3, 2]
print(longest_consecutive_substring(arr))