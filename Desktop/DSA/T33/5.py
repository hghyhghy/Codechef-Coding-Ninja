# Problem statement
# Given two non-decreasing sorted arrays, ‘A’ and ‘B’, having ‘N’ and ‘M’ elements, respectively.



# You must merge these arrays, ‘A’ and ‘B’, into a sorted array without using extra space. Of all the 'N + M' sorted elements, array 'A' should contain the first 'N' elements, and array 'B' should have the last 'M' elements.

def merge_sorted_array(arr1,arr2):
    
    i=0
    j=0
    
    merged_array=[]

    while i<len(arr1) and j <len(arr2):
        
        if arr1[i] < arr2[j]:
            
            merged_array.append(arr1[i])
            i+=1
            
        else:
            
            merged_array.append(arr2[j])
            j += 1
            
    
    while i<len(arr1):
        
        merged_array.append(arr1[i])
        i += 1
        
    while j<len(arr2):
        
        merged_array.append(arr2[j])
        j+=1
        
    return merged_array

arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]

print(merge_sorted_array(arr1,arr2))
