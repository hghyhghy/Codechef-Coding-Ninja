# Count Subarray sum Equals K

def counting_subarray(array,target):
    
    n=len(array)
    count = 0
    
    for i in range(n):
        
        temp = 0
        
        for j in range(i,n):
            
            temp += array[j]

            if temp ==  target:
                
                count = count +1
                
    
    return  count

arr = [1, 1, 1, 2, 3]
K = 3

print(counting_subarray(arr,K))