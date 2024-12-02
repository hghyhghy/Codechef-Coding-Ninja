
#intersection

def main(arr1,arr2):

    i=j=0
    
    r=[]
    while i<len(arr1) and j<len(arr2):
        
        if arr1[i] == arr2[j]:
            
            r.append(arr1[i]) 

            i +=1
            j +=1
            
        elif arr1[i]<arr2[j]:
            
            i +=1
            
        else:
            
            j +=1
            
    return r

arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))

print(main(arr1,arr2))
