# Problem statement
# Take an array with N elements with possibly duplicate elements as the input. The task is to find the index of the last occurrences of the element x in the array and, if it is not present, return -1.

# Detailed explanation ( Input/output f


def position_of_last_element(array:list[int],k:int)->int:
    
    n=len(array)
    last=-1
    
    for i in range(n-1,-1,-1):
        
        if array[i] == k:
            
            last=i
            break
    
    return last if last != -1 else -1

arr = [1, 2, 3, 2, 5, 2, 7]
x = 2
print(position_of_last_element(arr,x))