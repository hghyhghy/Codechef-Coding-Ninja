

#merge two sorted list

def main(arr1,arr2):
    
    i=j=0
    store=[]

    while i<len(arr1) and j<len(arr2):
        
        if arr1[i] == arr2[j]:
            
            store.append(arr1[i])

            i +=1
            
        else:
            
            store.append(arr2[j])
            j +=1
            
    
    while i <len(arr1):
        
        store.append(arr1[i])
        i +=1
        
    while j<len(arr2):
        
        store.append(arr2[j])
        j +=1
        
    return store

arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]

print(main(arr1,arr2))
    