
# search in the rotated sorted array 

def search_in_the_rotated_sorted_array(arr,target):

    for index,value in enumerate(arr):

        if value ==  target:

            return index
        
    return -1

nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

print(search_in_the_rotated_sorted_array(nums,target))