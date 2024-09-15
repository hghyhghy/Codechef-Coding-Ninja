# You are given an array 'arr' of size 'n' having unique elements that has been sorted in ascending order and rotated between 1 and 'n' times which is unknown.



# The rotation involves shifting every element to the right, with the last element moving to the first position. For example, if 'arr' = [1, 2, 3, 4] was rotated one time, it would become [4, 1, 2, 3].



# Your task is to find the minimum number in this array.

def minimum_in_sorted_array(array):
    
    smallest=array[0]

    for num in array:
        
        if num < smallest:
            
            smallest=num
            
    return smallest

a= [4, 1, 2, 3]
print(minimum_in_sorted_array(a))