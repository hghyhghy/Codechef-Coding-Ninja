
#intersection of the two sorted array 

def main(arr1,arr2):
    
    n=len(arr1)
    m=len(arr2)

    i=0
    j=0
    r=[]

    while i<n and j<m:
        
        if arr1[i] == arr2[j]:
            
            r.append(arr1[i])
            
            i +=1
            j +=1

        
        elif arr1[i] < arr2[j]:
            
            i +=1
            
        
        else:
            
            j+=1
            
    return r

a=list(map(int,input().split()))
b=list(map(int,input().split()))

print(main(a,b))

             
            
        