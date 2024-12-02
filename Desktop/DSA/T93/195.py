

#minimum subarray sum 

def main(array,target):
    
    n=len(array)
    min_length=float("inf")

    for i in range(n):
        
        curr=0
        
        for j in range(i,n):
            
            curr += array[j]

            if curr >= target:
                
                length =j-i+1
                
                min_length =min(min_length,length)

    return min_length
arr = [2, 3, 1, 2, 4, 3]
target = 7

print(main(arr,target))