

#max subarray contigous 

def main(array,k):
    
    n=len(array)
    
    for i in range(n):
        
        temp = 0
        
        for j in range(i-1,-1,-1):
            
            temp += array[j]
            
            if temp % k ==0:
                
                return True
            
            if i-j+1 >=2:
                
                break
            
    return False

n=int(input("enter"))
arr=list(map(int,input().split()))

print(main(arr,n))