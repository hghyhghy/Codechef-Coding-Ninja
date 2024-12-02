
#max min from the subarray 

def main(array,target):
    
    n=len(array)
    max_len=float("-inf")

    for i in range(n):
        
        curr= 0
        
        for j in range(i,n):
            
            curr += array[j]

            if curr == target:
                
                length  = j-i+1
                
                max_len =max(max_len,length)

                new_array=array[i:j+1]
                element1=max(new_array)
                element2=min(new_array)

    return element1 + element2

arr = [1, 2, 3, 4, 5]
target = 9

print(main(arr,target))