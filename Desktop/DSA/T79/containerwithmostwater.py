# Problem statement
# Given a sequence of ‘N’ space-separated non-negative integers A[1],A[2],A[3],......A[i]…...A[n]. Where each number of the sequence represents the height of the line drawn at point 'i'. Hence on the cartesian plane, each line is drawn from coordinate ('i',0) to coordinate ('i', 'A[i]'), here ‘i’ ranges from 1 to ‘N’. Find two lines, which, together with the x-axis forms a container, such that the container contains the most area of water.

# Note :
# 1. You can not slant the container i.e. the height of the water is equal to the minimum height of the two lines which define the container.

# 2. Do not print anything, you just need to return the area of the container with maximum water.

def most_water_area(array:list[int])->int:
    
    n=len(array)
    left=0
    right=n-1
    max_area= 0
    
    while left < right:
        
        width = right-left
        height=min(array[left],array[right])
        
        area = height * width
        
        max_area = max(max_area,area)
        
        if array[left] < array[right]:
            
            left +=1
            
        else:
            
            right -= 1
            
            
    return max_area
A = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(most_water_area(A))