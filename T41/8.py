# print sum of max na dmin element of the subarray 

def max_min_element_from_subarray(array,target):
    
    n=len(array)
    max_len=float('-inf')

    for start in range(n):
        
        current= 0
        
        for end in range(start,n):
            
            current += array[end]

            if current ==  target:
                
                lenght= end-start + 1
                
                max_len =max(max_len,lenght)
                
                new_array= arr[start:end+1]
                
                element1=max(new_array)
                element2=min(new_array)

                return element1+element2

    return None

arr = [1, 2, 3, 4, 5]
target = 9

print(max_min_element_from_subarray(arr,target))