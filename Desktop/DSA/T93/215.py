

#container with most water 

def main(array):
    
    n=len(array)
    left=0
    right=n-1
    area=0
    
    while left < right:
        
        width =  right-left
        height=min(array[right],array[left])

        total_area=width*height
        
        area=max(area,total_area)

        if array[left]< array[right]:
            
            left +=1
            
        else:
            
            right -=1
            
    return area

heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(main(heights))