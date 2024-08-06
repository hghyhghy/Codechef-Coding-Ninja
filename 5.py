# Kadane's Algorithm : Maximum Subarray Sum in an Array

def maximum_subarray(arr):
    
    n=len(arr)
    maxi=float('-inf')
    
    for i in range(n):
        
        for j in range(i,n):
            
            total_sum=0
            
            for k in range(i,j+1):
                
                total_sum += arr[k]

                maxi = max(maxi,total_sum)

    
    return maxi

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maximum_subarray(arr))