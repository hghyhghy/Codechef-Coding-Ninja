#string product less than k 

def main(array,k):
    
    n=len(array)
    count = 0
    
    for i in range(n):
        
        product=1
        
        for j in range(i,n):
            
            product *= array[j]

            if product < k:
                
                count +=1
                
            else:
                
                break
            
    return count

n=int(input("enter "))
ar=list(map(int,input().split()))
print(main(ar,n))