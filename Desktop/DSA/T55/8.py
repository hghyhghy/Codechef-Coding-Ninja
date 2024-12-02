# Given two 1-dimensional arrays containing strings of lowercase alphabets, print the elements that are common in both the arrays i.e. the strings that are present in both the arrays.

def common_string_between_two_arrays(arr1,arr2):
    
    set1=set(arr1)
    set2=set(arr2)

    common_points = set1.intersection(set2)

    return common_points

array1 = ["apple", "banana", "cherry", "date"]
array2 = ["banana", "date", "fig", "grape"]

print(common_string_between_two_arrays(array1,array2))