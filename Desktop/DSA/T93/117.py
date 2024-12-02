
#count pairs 
def main(array):
    
    n=len(array)
    count =0
    
    for i in range(n):
        
        for j in range(i+1,n):
            
            if array[j]-array[i] == j-i:
                
                count += 1
                
    return count

arr=list(map(int,input().split()))
print(main(arr))
                