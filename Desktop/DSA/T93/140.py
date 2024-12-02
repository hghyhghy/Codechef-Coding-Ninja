
#check consecutive

def main(array:list[int])->bool:
    
    n=len(array)
    array.sort()
    
    for i in range(1,n):
        
        if array[i] != array[i-1]+1:
            
            return False
        
    return True

nums=list(map(int,input().split()))
print(main(nums))
    
