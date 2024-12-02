
#check if consecutive 
def main(array):
    
    n=len(array)
    array.sort()
    
    for i in range(1,n):
        
        if array[i]-array[i-1] != 1:
            
            return False
        
    
    return True

arr = [4, 3, 5]
print(main(arr))