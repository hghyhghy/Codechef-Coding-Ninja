

#maximum subarray 

def main(array):
    
    n=len(array)
    max_sum=0
    max_length = 0
    
    for i in range(n):
        
        curr = 0
        
        for j in range(i,n):
            
            curr += array[j]

            if curr > max_sum:
                
                max_sum =max(max_sum,curr)
                length =j-i+1

                max_length = max(max_length,length)

    return max_length,max_sum

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(main(arr))