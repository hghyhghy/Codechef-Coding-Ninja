# Problem statement
# You are given a sorted integer array 'arr' of size 'n'.



# You need to remove the duplicates from the array such that each element appears only once.



# Return the length of this new array.



# Note:
# Do not allocate extra space for another array. You need to do this by modifying the given input array in place with O(1) extra memory. 

def remove_duplicates(array):
    
    new=[]
    n=len(array)
    
    for i in range(n):
        
        if array[i] == array[i-1]:
            
            continue
        
        new.append(array[i])

    return new

a=[1 ,2, 2, 2 ,3]
print(remove_duplicates(a))