# You are given an array 'arr' of length 'n'. Find the index(0-based) of a peak element in the array. If there are multiple peak numbers, return the index of any peak number.



# Peak element is defined as that element that is greater than both of its neighbors. If 'arr[i]' is the peak element, 'arr[i - 1]' < 'arr[i]' and 'arr[i + 1]' < 'arr[i]'.



# Assume 'arr[-1]' and 'arr[n]' as negative infinity.

def peak_element(array:list)->int:
    
    n=len(array)
    if n==1:
        
        return 0
    
    if n == 2:
        
        return 0 if array[0] >=array[1] else 1
    
    if array[0] > array[1]:
        
        return  0
    
    if array[n-1] > array[n-2]:
        
        return array[n-1]
    
    
    for i in range(1,n-1):
        
        if array[i-1]<array[i] > array[i+1]:
            
            return i
        
    return -1

arr = [1, 2, 3, 1]
print(peak_element(arr)) 