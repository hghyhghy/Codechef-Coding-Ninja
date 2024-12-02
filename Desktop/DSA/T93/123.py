
#subarray sum equal k

def main(array,k):
    
    current=0
    n=len(array)
    count=0
    i=0
    
    
    for j in range(n):
        
        current += array[j]
        
        while  current >k and i <= j:
            
            current -= array[i]
            i +=1
            
        if current == k:
            
            count +=1 
            
            
    return count

a=int(input("enter"))
arr=list(map(int,input().split()))

print(main(arr,a))