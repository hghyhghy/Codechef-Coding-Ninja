# check if the array  is sorted 
def checking_sorted_array(array):
    
    def bubble_sort(arr):
        
        n=len(arr)

        for i in range(n-1):
            
            for j in range(n-i-1):
                
                if arr[j] > arr[j+1]:
                    
                    arr[j],arr[j+1] = arr[j+1],arr[j]

        
        return arr
    
    array_copy = array.copy()
    sorted_version = bubble_sort(array_copy)

    if sorted_version == array:
        return "Sorted"
    else:
        return "Not Sorted"
    
array = [64, 34, 25, 12, 22, 11, 90]
print(checking_sorted_array(array))