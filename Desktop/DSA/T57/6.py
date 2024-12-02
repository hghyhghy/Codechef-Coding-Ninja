# Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray
#  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

class Solution:
    
    def minimum_subarray_sum(self,array,target):
        
        n=len(array)
        minimum=float("inf")

        for start in range(n):
            
            current = 0
            
            for end in range(start,n):
                
                current += array[end]

                if current >= target:
                    
                    minimum =min(minimum,end-start+1)
                    
                    break
        
        return minimum
    
    
sol = Solution()
nums = [2, 3, 1, 2, 4, 3]
target = 7
print(sol.minimum_subarray_sum(nums, target))