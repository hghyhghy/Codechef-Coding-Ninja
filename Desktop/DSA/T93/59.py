
#minimum in rotated sorted array 

def main(array:list[int]):
    
    if not array:
        
        not array
        
    minimum=array[0]

    for num in array:
        
        if num < minimum:
            
            minimum = num
            
    return minimum

arr=list(map(int,input().split()))
print(main(arr))
            