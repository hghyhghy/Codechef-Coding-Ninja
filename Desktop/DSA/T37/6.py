# Problem statement
# Ninja is given an array of integers that contain numbers in random order. He needs to write a program to find and return the number which occurs the maximum times in the given input. He needs your help to solve this problem.

# If two or more elements contend for the maximum frequency, return the element which occurs in the array first i.e. whose index is lowest.

def maximum_frequent_element(array):
    
    freq={}

    for num in array:
        
        if num in freq:
            
            freq[num] +=1
            
        else:
            
            freq[num]  = 1
            
            
    return [num for num,count in freq.items() if count > 1]
n=[ 1, 2, 3, 1, 2]

print(maximum_frequent_element(n))