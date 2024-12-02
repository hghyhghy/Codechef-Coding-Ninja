

#maximum subarray sum

def main(array):
    
    n=len(array)
    maximum=float("-inf")

    for i in range(n):
        
        curr = 0
        
        for  j in range(i,n):
            
            curr += array[j]

            maximum = max(maximum,curr)

    return maximum

arr = [1, -2, 3, 4, -1, 2, 1, -5, 4]
print(main(arr))