# You are given an array 'arr' of length 'n'. Find the index(0-based) of a peak element in the array. If there are multiple peak numbers, return the index of any peak number.



# Peak element is defined as that element that is greater than both of its neighbors. If 'arr[i]' is the peak element, 'arr[i - 1]' < 'arr[i]' and 'arr[i + 1]' < 'arr[i]'.



# Assume 'arr[-1]' and 'arr[n]' as negative infinity.



# Note:
# 1.  There are no 2 adjacent elements having same value (as mentioned in the constraints).
# 2.  Do not print anything, just return the index of the peak element (0 - indexed).
# 3. 'True'/'False' will be printed depending on whether your answer is correct or not.

def finding_peak_element(array):
    
    if not array or len(array) < 3:
        
        return None
    
    n=len(array)

    for i in range(1,n-1):
        
        if  array[i] > array[i+1] and array[i] > array[i-1]:
            
            return i

    return None

a=[1, 8, 1, 5, 3]
print(finding_peak_element(a))
