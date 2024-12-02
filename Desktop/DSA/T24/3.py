# Check if Array is a subset of another array or not

def checking_subset_or_not(arr1,arr2):
    
    arr1.sort()
    arr2.sort()

    i=j=0
    
    while i < len(arr1) and j < len(arr2):
        
        if arr1[i] == arr2[j]:
            
            j += 1
            
        i += 1
    
    
    return j == len(arr2)

arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 3, 5]

print(checking_subset_or_not(arr1,arr2))