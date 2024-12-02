# Problem statement
# For a given array with N elements, you need to find the length of the longest subsequence from the array such that all the elements of the subsequence are sorted in strictly increasing order.

# Strictly Increasing Sequence is when each term in the sequence is larger than the preceding term.

# For example:
# [1, 2, 3, 4] is a strictly increasing array, while [2, 1, 4, 3] is not.

def longest_increasing_subsequence(array:list)->int:
    
    if not array:
        
        return 0
    
    list1=[]

    for num in array:
        
        if not list1 or num>list1[-1]:
            
            list1.append(num)

        else:
            
            for i in range(len(list1)):
                
                if list1[i] > num:
                    
                    list1[i]= num
                    break
                
    return len(list1)

arr = [3,7,4,6]
print(longest_increasing_subsequence(arr))