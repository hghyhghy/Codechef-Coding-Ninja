
#reverse first k  elements 

def main(array,k):
    
    n=len(array)
    if n < k:
        
        return 0
    
    start=0
    end=k-1
    
    while start < end:
        
        array[start],array[end]=array[end],array[start]

        start +=1
        end -=1
        
    return array

arr = [1, 2, 3, 4, 5]
k = 3

print(main(arr,k))
    