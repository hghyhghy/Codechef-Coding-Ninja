# sort the numbers by increasing frequency 

from collections import Counter

def sort_by_frequency(array):
    
    frequency = Counter(array)
    
     # Return a tuple (frequency of x, value of x)
    sorted_nums=sorted(array, key=lambda x : (frequency[x],x))
    
    return sorted_nums

nums = [1, 1, 2, 3, 2, 2, 4, 1]
print(sort_by_frequency(nums))

