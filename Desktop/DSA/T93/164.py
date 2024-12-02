

#intersection of two arrays 

def main(arr1,arr2):
    
    arr1.sort()
    arr2.sort()

    r=[]
    i=j=0
    
    while i<len(arr1)  and j < len(arr2):
        
        if arr1[i] == arr2[j]:
            
            r.append(arr1[i])

            i +=1
            j +=1
            
        elif arr1[i] < arr2[j]:
            
            i +=1
            
        else:
            
            j +=1 
            
    return r

arr1 = [1, 2, 2, 3, 4]
arr2 = [2, 3, 5]
print(main(arr1,arr2))