# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

# Since the result may be very large, so you need to return a string instead of an integer.

def largest_number(array):
    
    nums_str=list(map(str,array))

    nums_str.sort(key=lambda x : x*10 , reverse=True)
    largest_sum = "".join(nums_str)

    if largest_sum[0] == "0":
        
        return "0"

    return largest_sum

nums = [3, 30, 34, 5, 9]
print(largest_number(nums))