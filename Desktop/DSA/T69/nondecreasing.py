# Problem statement
# You have been given an integer array/list 'ARR' of size 'N'. Write a solution to check if it could become non-decreasing by modifying at most 1 element.

# We define an array as non-decreasing, if ARR[i] <= ARR[i + 1] holds for every i (0-based) such that (0 <= i <= N - 2).

def non_decreasing_array(array:list)->bool:
    
    count= 0
    n=len(array)

    for i in range(n-1):
        
        if array[i] > array[i+1]:
            
            count += 1
            
            if count > 1:
                
                return False
            
            
            if i == 0 or array[i-1]<=array[i+1]:
                
                array[i]=array[i+1]
                
            else:
                
                array[i+1] = array[i]

    return True

arr = [4, 2, 3]
print(non_decreasing_array(arr))