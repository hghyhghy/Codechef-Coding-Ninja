
#common in three array 

def main(arr1,arr2,arr3):
    
    a=len(arr1)
    b=len(arr2)
    c=len(arr3)
    
    
    i=j=k= 0
    result=[]

    while  i<a and j<b and k<c:
        
        if  arr1[i] == arr2[j] == arr3[k]:
            
            if not result or result[-1] != arr1[i]:
                
                result.append(arr1[i])

            i +=1
            j +=1
            k +=1
            
        
        elif arr1[i] < arr2[j]:
            
            i +=1
            
        elif arr2[j]  < arr3[k]:
            
            j +=1
            
        else:
            
            k +=1
            
    return result

a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))

print(main(a,b,c))
