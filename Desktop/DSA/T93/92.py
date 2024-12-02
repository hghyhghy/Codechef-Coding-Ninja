
#k pair with smallest sum 

def main(arr1,arr2,k):

    result=[]

    for x in arr1:
        
        for y in arr2:
            
            result.append((x,y))

    
    result.sort(key=lambda x:x[0]+x[1])
    
    return result[:k]

arr1=[1, 7, 11]
arr2=[2,4,6]
k=3

print(main(arr1,arr2,k))
