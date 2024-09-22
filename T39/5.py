# You are given ‘K’ lists containing non-negative integers. Each list has a size ‘N’ and is sorted in non-decreasing order. You need to find the minimum length of a range such that at least one element of each list must be included in that range.

# For example :

# If we have 3 lists as [1, 10, 11], [2, 3, 20], [5, 6, 12] then the [1, 5] is the range that includes 1 from the first list, 2,3 from the second list, and 5 from the third list i.e, this range contains at least one element from each list.

def smallest_element_from_k_sorted_list(array):
    
    smallest_elemnt=float('inf')
    index=-1
    
    for i,element in enumerate(array):
        
        if element and element[0]<smallest_elemnt:
            
            smallest_elemnt=element[0]
            index = i
            
            
    return smallest_elemnt if index != -1 else None

k_sorted_lists = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]

print(smallest_element_from_k_sorted_list(k_sorted_lists))