

#rotate 

def rotate(arr,start,end):
    
    while start  < end:
        
        arr[start],arr[end]=arr[end],arr[start]
        
        start +=1
        end -=1
        

def main(arr,k):
    
    n=len(arr)
    k =k %n 
    
    rotate(arr,0,n-1)
    
    rotate(arr,0,n-k-1)
    
    rotate(arr,n-k,n-1)

    return arr

arr = [1,2,3,4,5]
k=2

print(main(arr,k))