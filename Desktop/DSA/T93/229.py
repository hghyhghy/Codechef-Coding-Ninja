
#minimum in rotated sorted arry

def main(array):
    
    smallest=array[0]
    
    for num in array:
        
        if num<smallest:
            
            smallest =  num
            
    return smallest

nums=list(map(int,input().split()))
print(main(nums))