# Problem statement
# You have been given an array/list ‘ARR‘ of length ‘N’ consisting of non-negative integers ARR1, ARR2, ..., ARRN. The i’th integer denotes a point with coordinates (i, ARR[i]). ‘N’ vertical lines are drawn such that the two endpoints of the i’th line are at (i, arr[i]) and (i,0).

# Your task is to find two lines, which, together with the x-axis, form a container, such that the container contains the most water. Return the maximum area of the container.

def container_with_max_water(array):
    
    n=len(array)
    max_area=0
    
    for i in range(n):
        
        for j in range(i+1,n):
            
            height = min(array[i],array[j])

            width = j-i
            area = height*width
            
            max_area=max(max_area,area)

    return max_area

arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(container_with_max_water(arr))