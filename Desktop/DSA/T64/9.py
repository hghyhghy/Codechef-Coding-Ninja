# Ninja is given an array of integers that contain numbers in random order. He needs to write a program to find and return the number which occurs the maximum times in the given input. He needs your help to solve this problem.

# If two or more elements contend for the maximum frequency, return the element which occurs in the array first i.e. whose index is lowest.

# For example,

# For 'arr' = [ 1, 2, 3, 1, 2]. you need to return 1. using dict

def most_fre_element(array):
    
    freq={}
    occurance={}

    for index,num in enumerate(array):
        
        if num in freq:
            
            freq[num] += 1
            
        else:
            
            freq[num] = 1
            occurance[num] = index
            
    
    frequent= -1
    max_freq=None
    
    for num,count in freq.items():
        
        if count > frequent:
            
            frequent = count
            max_freq = num
            
        elif count == frequent:
            
            if occurance[num] < occurance[max_freq]:
                
                max_freq = num
                
    return max_freq

arr = [2 ,1, 3, 1, 2]
print(most_fre_element(arr))