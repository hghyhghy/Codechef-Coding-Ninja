

#add two arrays 

def main(arr1,arr2):
    
    i=0
    j=0
    
    r=[]

    while i<len(arr1) and j<len(arr2):
        
        store=(arr1[i]+arr2[j])

        r.append(store)

        i +=1
        j +=1
        
    
    return r

arr1 = [1, 2, 3]
arr2 = [4, 5, 6]

print(main(arr1,arr2))