#  Merge K Sorted Arrays
# Moderate
# 0/80
# Average time to solve is 15m
# 208 upvotes
# Asked in companies
# Problem statement
# You have been given ‘K’ different arrays/lists, which are sorted individually (in ascending order). You need to merge all the given arrays/list such that the output array/list should be sorted in ascending order.

def merge_k_sorted_array(array:list)->list:
    
    merged=[]

    for num in array:
        
        merged.extend(num)

    
    merged.sort()

    return merged

arrays = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [0, 10, 11]
]

print(merge_k_sorted_array(arrays))