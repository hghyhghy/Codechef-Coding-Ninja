# Given two 1-dimensional arrays containing strings of lowercase alphabets, print the elements that are common in both the arrays i.e. the strings that are present in both the arrays.

# Note:
# An element of one array can be mapped only to one element of the array. For example :

# Array 1 = {“ab”, “dc”, “ab”, “ab”}
# Array 2 = {“dc”, “ab”, “ab”} 

# The common elements for the above example will be “dc”, “ab”, and “ab”. 

def common_element(arr1:list[str],arr2:list[str])->list[str]:
    
    common=[]
    store=arr1[:]

    for char in arr2:
        
        if char in store:
            
            common.append(char)
            store.remove(char)

    
    return common

arr1 = ["ab", "dc", "ab", "ab"]
arr2 = ["dc", "ab", "ab"]
print(common_element(arr1,arr2))