

#search an element

def main(array,target):
    
    n=len(array)

    for i in range(n):
        
        if array[i] == target:
            
            return array[i],i
        
    
    return -1

rotated_array = [4, 5, 1, 2, 3]
t=1

print(main(rotated_array,t))