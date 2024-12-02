# You have been given an array/list ‘ARR‘ of length ‘N’ consisting of non-negative integers ARR1, ARR2, ..., ARRN. The i’th integer denotes a point with coordinates (i, ARR[i]). ‘N’ vertical lines are drawn such that the two endpoints of the i’th line are at (i, arr[i]) and (i,0).

# Your task is to find two lines, which, together with the x-axis, form a container, such that the container contains the most water. Return the maximum area of the container

def contaier_most_water(array):
    
    left=0
    right=len(array) - 1
    
    area=0
    
    while left < right:
        
        width= right-left
        height=min(array[left],array[right])

        total_area=width*height

        area=max(area,total_area)

        if array[left] < array[right]:
            
            left += 1
        else:
            
            right -= 1
            
    return area

heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]

print(contaier_most_water(heights))