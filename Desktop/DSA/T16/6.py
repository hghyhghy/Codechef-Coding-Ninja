# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 
def house_robber(array):
    
    if not array:
        
        return 0
    
    if len(array) == 0:
        
        return array[0]

    prev1=0
    prev2=0
    # prev1 represents the maximum money robbed up to the house before the previous house.
    # prev2 represents the maximum money robbed up to the previous house.
    
    for num in array:
        
        current = max(num+prev2,prev1)
        prev1=prev2
        prev2 =  current
        
    return prev2

nums = [10,11,56]
print(house_robber(nums))