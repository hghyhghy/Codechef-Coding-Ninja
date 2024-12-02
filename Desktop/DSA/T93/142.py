

#subarry sum upto zero

def main(array:list[int])->list[int]:
    
    n=len(array)
    
    
    for i in range(n):
        
        current = 0
        
        for j in range(i,n):

            current += array[j]

            if current == 0:
                
                subarray=array[i:j+1]
                
    return subarray

arr = [3, 4, -7, 1, 2, -6, 1, 3, -2, -1]
print(main(arr))