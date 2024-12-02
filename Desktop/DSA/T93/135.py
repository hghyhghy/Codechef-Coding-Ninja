

#common elements 

def main(arr1,arr2,arr3):
    
    i=j=k=0
    r=set()

    while i<len(arr1) and j<len(arr2) and k<len(arr3):
        
        if arr1[i] == arr2[j] == arr3[k]:
            
            r.add(arr1[i])
            
            i +=1
            j +=1
            k +=1
            
        
        elif  arr1[i] < arr2[j]:
            
            i +=1
            
        elif arr2[j] < arr3[k]:
            
            j +=1
            
        else:
            
            k +=1
            
    return sorted(r)

A = [1, 5, 10, 20, 30]
B = [5, 13, 15, 20]
C = [5, 20]

print(main(A,B,C))