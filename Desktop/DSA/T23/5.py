# Rotate array by K elements - Block Swap Algorithm

def rotate(arr,start,end):
    
    while start < end:
        
        arr[start],arr[end]= arr[end],arr[start]

        start += 1
        end -= 1
        
        
def main_function(arr,k):
    
    n=len(arr)

    k=k%n
    
    rotate(arr,0,n-1)
    
    rotate(arr,0,k-1)
    
    rotate(arr ,k ,n-1)
    

    
    return arr


array= [1,2,3,4,5] 
k=2

print(main_function(array,k))