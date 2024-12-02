

#longest subarray with sum  k

def main(array,k):
    
    n=len(array)
    maximum=float("-inf")

    for i in range(n):
        
        curr= 0
        
        for j in range(i,n):
            
            curr += array[j]

            if curr == k:
                
                length = j-i+1
                
                maximum=max(maximum,length)

    return maximum

arr = [1, 2, 3, 4, 5, -2, -3, 6]
K = 7

print(main(arr,K))