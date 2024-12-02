# Problem statement
# You have been given ‘K’ different arrays/lists, which are sorted individually (in ascending order). You need to merge all the given arrays/list such that the output array/list should be sorted in ascending order.

def merge_two_sorted_list(a1,a2):
    
    combined=a1+a2
    
    return sorted(combined)

list1 = [3, 1, 4, 1, 5]
list2 = [9, 2, 6, 5, 3]

print(merge_two_sorted_list(list1,list2))