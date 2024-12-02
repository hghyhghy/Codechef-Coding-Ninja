# Problem statement
# Aahad and Harshit always have fun by solving problems. Harshit took a sorted array consisting of distinct integers and rotated it clockwise by an unknown amount. For example, he took a sorted array = [1, 2, 3, 4, 5] and if he rotates it by 2, then the array becomes: [4, 5, 1, 2, 3].

# After rotating a sorted array, Aahad needs to answer Q queries asked by Harshit, each of them is described by one integer Q[i]. which Harshit wanted him to search in the array. For each query, if he found it, he had to shout the index of the number, otherwise, he had to shout -1.

# For each query, you have to complete the given method where 'key' denotes Q[i]. If the key exists in the array, return the index of the 'key', otherwise, return -1.

# Note:

# Can you solve each query in O(logN) ?

def search_in_roated_sorted_array(array:list,target:int)->int:
    
    
    n=len(array)

    for i in range(n):
        
        if array[i] == target:
            
            return i
        
    return -1

nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

print(search_in_roated_sorted_array(nums,target))