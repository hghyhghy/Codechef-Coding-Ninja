# Problem statement
# You have been given an integer array/list(ARR) of size N. Where N is equal to [2M + 1].

# Now, in the given array/list, 'M' numbers are present twice and one number is present only once.

# You need to find and return that number which is unique in the array/list.

#  Note:
# Unique element is always present in the array/list according to the given condition.

def unique(array):
    
    freq={}

    for num in array:
        
        if num in freq:
            
            freq[num] += 1
            
        else:
            
            freq[num] = 1
            
    for num,count in freq.items():
        
        if count ==1:
            
            return num
        
    return -1
arr = [2, 3, 5, 4, 5, 3, 4]
print(unique(arr))