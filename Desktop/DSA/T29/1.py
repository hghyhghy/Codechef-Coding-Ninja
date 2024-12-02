# Problem statement
# Aahad and Harshit always have fun by solving problems. Harshit took a sorted array consisting of distinct integers and rotated it clockwise by an unknown amount. For example, he took a sorted array = [1, 2, 3, 4, 5] and if he rotates it by 2, then the array becomes: [4, 5, 1, 2, 3].

# After rotating a sorted array, Aahad needs to answer Q queries asked by Harshit, each of them is described by one integer Q[i]. which Harshit wanted him to search in the array. For each query, if he found it, he had to shout the index of the number, otherwise, he had to shout -1.


def search_in_the_rotated_sorted_array(arr,target):
    
    
    for index in range(len(arr)):
        
        if arr[index] == target:
            
            return index,target
        
    
    return -1

rotated_array = [4, 5, 1, 2, 3]
t=1
print(search_in_the_rotated_sorted_array(rotated_array,t))