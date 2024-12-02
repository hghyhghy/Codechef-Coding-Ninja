# Count triplets with sum smaller than a given value
# Last Updated : 18 Mar, 2024
# Given an array of distinct integers and a sum value. Find count of triplets with sum smaller than given sum value. The expected Time Complexity is O(n2).
# Examples: 
 

# Input : arr[] = {-2, 0, 1, 3}
#         sum = 2.
# Output : 2
# Explanation :  Below are triplets with sum less than 2
#                (-2, 0, 1) and (-2, 0, 3) 

# Input : arr[] = {5, 1, 3, 4, 7}
#         sum = 12.
# Output : 4
# Explanation :  Below are triplets with sum less than 12
#                (1, 3, 4), (1, 3, 5), (1, 3, 7) and 
#                (1, 4, 5)

def triplet_sum_less_than_k(array,target):
    
    count = 0
    array.sort()
    n=len(array)

    for i in range(n):
        
        for j in range(i+1,n):
            
            for k  in range(j+1,n):
                
                if (array[i]+array[j]+array[k]) < target:
                    
                    count += 1

    return count

arr = [-2, 0, 1, 3]
t=2

print(triplet_sum_less_than_k(arr,t))
            
            