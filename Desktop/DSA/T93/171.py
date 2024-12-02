


#first and last position of an element 

def main(array,target):
    
    n=len(array)
    first=-1
    last=-1
    
    for i in range(n):
        
        if array[i] ==  target:
            
            first = i
            break
        
    
    for j in range(n):

        if array[j] == target:
            last = j
            
    
    return first,last if first and last else -1

arr = [1, 2, 3, 4, 2, 5, 2, 6]
target = 2

print(main(arr,target))