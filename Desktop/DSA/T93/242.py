
#finding the insert position 

def main(arr,target):
    
    n=len(arr)
    
    for i in range(n):
        
        if arr[i] == target:
            
            return i
        
        else:
            
            if target < arr[i]:
                
                return i
            
    return n

arr = [1, 2, 4, 7]
m = 6 

print(main(arr,m))