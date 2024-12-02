# You have been given an array/list ‘ARR‘ of length ‘N’ consisting of non-negative integers ARR1, ARR2, ..., ARRN. The i’th integer denotes a point with coordinates (i, ARR[i]). ‘N’ vertical lines are drawn such that the two endpoints of the i’th line are at (i, arr[i]) and (i,0).

# Your task is to find two lines, which, together with the x-axis, form a container, such that the container contains the most water. Return the maximum area of the container.

def max_area1(array:list[int])->int:
    
    n=len(array)
    left=0
    right = n-1
    max_area  = float("-inf")
    
    
    while left < right:
        
        height = min(array[left],array[right])
        
        width =  right-left
        
        area =  height*width
        
        max_area = max(max_area,area)
        
        if array[left]<array[right]:
            
            left +=1
            
        else:
            
            right  -= 1
            
    
    return max_area

arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(max_area1(arr))