
#three sum 

def main(arr):
    
    n=len(arr)
    see=set()
    arr.sort()

    
    for i in range(n):
        
        for j in range(i+1,n):
            
            for k in range(j+1,n):
                
                if arr[i] + arr[j] + arr[k] == 0:
                    
                    see.add((arr[i],arr[j],arr[k]))

    
    return list(see)

arr = [-1, 0, 1, 2, -1, -4]
print(main(arr))