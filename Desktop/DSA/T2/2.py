# Given an array of integers, such as [5, 2, 4, 1, 3], and an integer sum, such as 9, the algorithm should determine that the pair (a, b) = (2, 7) or (4, 5) satisfies the condition a + b = sum. If no such pair exists, the algorithm should return -1.

def calculate_sum(arr,target):
    
    store=[]
    for i in range(len(arr)):
        
        for j in range(i+1,len(arr)):
            
            if arr[i] + arr[j] == target:
                
                store.append([arr[i],arr[j]])


    return store

a=[5, 2, 4, 1, 3]
t=9

print(calculate_sum(a,t))