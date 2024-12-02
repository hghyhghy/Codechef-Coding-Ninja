# You are given an unsorted array/list 'ARR' of 'N' integers. Your task is to return the length of the longest consecutive sequence.

# The consecutive sequence is in the form ['NUM', 'NUM' + 1, 'NUM' + 2, ..., 'NUM' + L] where 'NUM' is the starting integer of the sequence and 'L' + 1 is the length of the sequence.

# Note:

# If there are any duplicates in the given array we will count only one of them in the consecutive sequence.

def longest_consecutive(arr):
    
    arr.sort()
    longest = 0
    arr=list(set(arr))

    n=len(arr)

    for i in range(n):
        
        custom_lenght =1
        
        
        for j in range(i+1,n):
            
            if arr[j] == arr[j-1] +1:
                
                custom_lenght += 1
                
            else:
                
                break
            
        longest = max(longest,custom_lenght)

    return longest

arr = [100, 4, 200, 1, 3, 2]
print(longest_consecutive(arr))