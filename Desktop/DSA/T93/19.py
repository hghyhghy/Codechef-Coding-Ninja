#container with most water 

def main(array:list[int])->int:
    
    n=len(array)
    left=0
    right=n-1
    maximum=float("-inf")

    while left  < right:
        
        height=min(array[left],array[right])

        widtth=right-left
        
        area=height*widtth
        
        maximum=max(maximum,area)
        
        if array[left] < array[right]:
            
            left += 1
            
        else:
            
            right -=1
            
    return maximum

arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(main(arr))

        