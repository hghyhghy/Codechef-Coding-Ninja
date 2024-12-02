

#subaray divisbile by k 

def main(array,k):
    
    n=len(array)
    count  = 0
    
    for i in range(n):
        
        current = 0
        
        for j in range(i,n):
            
            current += array[j]

            if current % k == 0:
                
                count += 1
                
    return count

n=int(input("enter"))
array=list(map(int,input().split()))

print(main(array,n))               
                