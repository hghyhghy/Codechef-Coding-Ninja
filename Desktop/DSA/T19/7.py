

# Code
# Testcase
# Test Result
# Test Result
# 862. Shortest Subarray with Sum at Least K
# Hard
# Topics
# Companies
# Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.

# A subarray is a contiguous part of an array.

 

def shortest_subarray_wuth_minimum_lenght(array,k):
     
    n=len(array)
    min_lenght=float('inf')

    for start in range(n):
        
        total_sum=0
        
        for end in range(start,n):
            
            total_sum += array[end]

            if total_sum >=k:
                
                min_lenght=min(min_lenght,end-start+1)
                
                break

    return min_lenght

nums = [1, 2, 3, 4, 5]
k = 11

print(shortest_subarray_wuth_minimum_lenght(nums,k))