# Problem statement
# You are given a non-decreasing array 'arr' consisting of 'n' integers and an integer 'x'. You need to find the first and last position of 'x' in the array.

def first(arr,target):
    
    for i in range(len(arr)):
        
        if arr[i] ==  target:
            
            return i
    
    return -1

def from_last(arr,target):
    
    for i in range(len(arr)-1,-1,-1):
        
        if arr[i] == target:
            
            return i
        
    return -1

def main_functin(arr,x):
    
    first_element= first(arr,x)

    last_element=from_last(arr,x)

    return first_element,last_element


arr = [1, 2, 2, 2, 3, 4, 5]
x = 2

print(main_functin(arr,x))