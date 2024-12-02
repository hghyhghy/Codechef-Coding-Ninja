# Problem statement
# You have been given two arrays/list ‘ARR1’ and ‘ARR2’ consisting of ‘N’ and ‘M’ integers respectively. Your task is to return the number of elements common to ‘ARR1’ and ‘ARR2’ and the number of elements in the union of ‘ARR1’ and ‘ARR2’.

# Example:
# Let’s assume ‘ARR1’ is [1,2,3,4,5] and ‘ARR2’ is [2,4,6,8]. Elements common to ‘ARR1’ and ‘ARR2’ are [2,4] as they occur in both ‘ARR1’ and ‘ARR2’. Therefore the number of elements common to ‘ARR1’ and ‘ARR2’ is 2. Union of ‘ARR1’ and ‘ARR2’ is [1,2,3,4,5,6,8]. Therefore the number of distinct elements in the union of ‘ARR1’ and ‘ARR2’ is 7. So, the answer will be 2 7.

def common_and_union(arr1:list,arr2:list)->list:
    
    n1=set(arr1)
    n2=set(arr2)
    
    common=n1.intersection(n2)
    distinct = n1.union(n2)
    
    return len(common),len(distinct)

arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8]

print(common_and_union(arr1,arr2))