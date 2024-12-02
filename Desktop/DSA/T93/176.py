

#subarray with distinct element 

def main(array):
    
    n=len(array)
    result=[]

    for i in range(n):
        
        seen=set()

        for j in range(i,n):
            
            if array[j] in seen:
                
                break
            
            seen.add(array[j])
            result.append(array[i:j+1])
            
    return result

arr = [1, 2, 3, 2, 1]
print(main(arr))