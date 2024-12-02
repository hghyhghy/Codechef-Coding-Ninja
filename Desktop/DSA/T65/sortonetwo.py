# Problem statement
# You have been given an integer array/list(ARR) of size N that contains only integers, 0 and 1. Write a function to sort this array/list. Think of a solution which scans the array/list only once and don't require use of an extra array/list.

# Note:
# You need to change in the given array/list itself. Hence, no need to return or print anything. 

def sort_one_two(array:list)->list:
    
    zero=array.count(0)

    one=len(array) - zero
    
    array[:zero] = [0]*zero
    array[zero:] =[1]*one
    
    return array

arr = [1, 0, 1, 0, 1, 0]
print(sort_one_two(arr))