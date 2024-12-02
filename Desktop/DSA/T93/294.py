

#reverse array

def main(array):
    
    n=len(array)
    left = 0
    right =n-1
    
    while left < right:
        
        array[left],array[right]=array[right],array[left]

        left +=1
        
        right -=1
        
    return array

array = [1, 2, 3, 4, 5]
print(main(array))