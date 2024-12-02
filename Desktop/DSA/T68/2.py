# You have been given an array/list 'ARR' of integers. Your task is to find the second largest element present in the 'ARR'.

# Note:
# a) Duplicate elements may be present.

# b) If no such element is present return -1.
# Example:
# Input: Given a sequence of five numbers 2, 4, 5, 6, 8.

def second_largest_element(array:list)->int:
    
    new= set()
    n=len(array)

    for i in range(n):
        
        if array[i] in new:
            
            continue
        
        new.add(array[i])

    new_array=sorted(new,reverse=True)

    return new_array[1]

a=[2,1,2,4,5,5]
print(second_largest_element(a))