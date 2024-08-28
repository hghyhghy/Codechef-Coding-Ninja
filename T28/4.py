# Problem statement
# You are given a sorted integer array 'arr' of size 'n'.



# You need to remove the duplicates from the array such that each element appears only once.



# Return the length of this new array.

def remove_duplicates(array):
    
    if not array:
        
        return 0
    
    j=0
    
    for i in range(1,len(array)):
        
        if array[i]  != array[j]:
            
            j += 1
            
            array[j] = array[i]

    
    return j+1

arr = [1, 1, 2, 3, 3, 4, 5]
print(remove_duplicates(arr))