
#three sum closest

def main(array,target):
    
    n=len(array)
    clsest=float("inf")

    for i in range(n):
        
        for j in range(i+1,n):
            
            for k in range(j+1,n):
                
                current =  array[i] + array[j] + array[k]

                if abs(current-target) < abs(clsest-target):
                    
                    clsest = current
                    
    return clsest

arr = [-1, 2, 1, -4]
target = 1

print(main(arr,target))

