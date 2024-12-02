# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.


def missing_integers(array):
    
    n=len(array)
    store=set(array)

    result=[num for num in range(1,n+1) if num not in store]

    return result

nums = [4, 3, 2, 7, 8, 2, 1, 4]
print(missing_integers(nums))