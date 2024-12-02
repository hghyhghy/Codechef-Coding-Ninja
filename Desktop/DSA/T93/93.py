

#max subarray sum

def main(array):
    
    n=len(array)
    max_sum =float("-inf")
    
    for i in range(n):
        
        current= 0
        
        for j in range(i,n):
            
            current += array[j]

            max_sum = max(max_sum,current)

    return max_sum if max_sum >0  else -1

num=list(map(int,input().split()))
print(main(num))