# The function accepts an integer array ‘arr’ of size ‘n’ and an integer ‘d’ as its argument. The function needs to rotate the array ‘arr’ by ‘d’ positions to the right. The rotation should be done in place, without using any additional memory.

def rotate_array(arr,start,end):
    
    while start < end :
        
        arr[start],arr[end] = arr[end],arr[start]

        start += 1
        end -= 1
        
        
def operation(arr,d):
    
    n=len(arr)
    d=d%n
    
    rotate_array(arr,0,n-1)
    
    rotate_array(arr,0,d-1)

    rotate_array(arr,d,n-1)
    
    return arr


arr=[ 1, 2, 3, 4 ,5]

d= 3

print(operation(arr,d))


