# Problem statement
# Given a binary array 'ARR' of size 'N', your task is to find the longest sequence of continuous 1’s that can be formed by replacing at-most 'K' zeroes by ones. Return the length of this longest sequence of continuous 1’s.

def maximum_consecutive_one(array):
    
    n=len(array)
    max_count=0
    
    for i in range(n):
        
        count = 0
        
        for j in range(i,n):
            
            if array[j] ==  1:
                
                count += 1
                max_count =  max(max_count,count)

            else:
                
                break
            
    return max_count

arr = [1, 1, 0, 1, 1, 1, 0, 1, 1]

print(maximum_consecutive_one(arr))