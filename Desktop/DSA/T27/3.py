# Problem statement
# You have been given a sorted array/list 'arr' consisting of ‘n’ elements. You are also given an integer ‘k’.



# Now the array is rotated at some pivot point unknown to you.



# For example, if 'arr' = [ 1, 3, 5, 7, 8], then after rotating 'arr' at index 3, the array will be 'arr' = [7, 8, 1, 3, 5].



# Now, your task is to find the index at which ‘k’ is present in 'arr'.

def find_element_in_rotated_sorted_array(arr,element):
    
    for index in range(len(arr)):
        
        if arr[index] == element:
            
            return index
        
        
    
    return -1

arr = [7, 8, 1, 3, 5]
k = 3
print(find_element_in_rotated_sorted_array(arr,k))