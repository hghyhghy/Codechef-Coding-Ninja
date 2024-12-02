# Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

def remove_unique_duplicates(array):
    
    count = 1
    unique_index= 1
    
    for i in range(1,len(array)):
        
        if array[i] == array[i-1]:
            
            count += 1
            
        else:
            
            count = 1 
            
            
        if count <=2 :
            
            array[unique_index] = array[i]
            unique_index += 1
            
            
    return unique_index

nums = [1, 1, 1, 2, 2, 3]
length = remove_unique_duplicates(nums)
print("Array after removing duplicates:", nums[:length])