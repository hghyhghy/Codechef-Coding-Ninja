

#pair with  diff equl target

def main(array,target):
    
    n=len(array)
    r=[]

    for i in range(n):
        
        for j in range(i+1,n):
            
            if abs(array[i]-array[j]) == target:
                
                r.append([array[i],array[j]])

    return r

arr = [1, 5, 3, 4, 2]
k=3

print(main(arr,k))