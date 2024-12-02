

#reverse after position

def main(array,k):
    
    n=len(array)
    start=k+1
    end=n-1
    
    while start < end:
        
        array[start],array[end] = array[end],array[start]

        start +=1
        
        end -=1
        
    return array

arr = [1, 2, 3, 4, 5, 6]
M = 3

print(main(arr,M))