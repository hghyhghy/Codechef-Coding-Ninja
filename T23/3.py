# rearrange the array in increasing _ decreasing order 

from collections import Counter

def order_of_frequency(arr):
    
    frequency= Counter(arr)

    temp_order = sorted(arr,key=lambda x : (frequency[x],x))

    return temp_order

nums = [1, 1, 2, 3, 2, 2, 4, 1]
print(order_of_frequency(nums))