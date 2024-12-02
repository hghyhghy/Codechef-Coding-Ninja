# You are given an array/list ARR consisting of N integers. Your task is to find the length of the longest decreasing subsequence.

# A subsequence is a sequence of numbers obtained by deleting zero or more elements from the array/list, keeping the relative positions of elements same as it was in the initial sequence. A decreasing subsequence is a subsequence in which every element is strictly less than the previous number.

# Note:

# There can be more than one subsequences with the longest length.
# For example:-
# For the given array [5, 0, 3, 2, 9], the longest decreasing subsequence is of length 3, i.e. [5, 3, 2]

def longest_decreasing_subsequence(array:list[int])->int:
    
    stack=[]
    
    for num in array:
        
        if not stack or stack[-1]>num:
            
            stack.append(num)
            
        else:
            
            for i in range(len(stack)):
                
                if stack[i] <= num:
                    
                    stack[i] =num
                    break
                
    return len(stack)

arr = [5, 0, 3, 2, 9]
print(longest_decreasing_subsequence(arr))