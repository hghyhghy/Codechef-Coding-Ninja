# Problem statement
# You are given a sorted array ‘arr’ of ‘n’ numbers such that every number occurred twice in the array except one, which appears only once.



# Return the number that appears once.

def single_element_from_the_array(arr):
    
    freq = {}

    for num in arr:
        
        if num in freq:
            
            freq[num] += 1
            
        else:
            
            freq[num] = 1
            
    result=[num for num,count in freq.items() if count == 1]

    return result

a= [1,1,2,2,4,5,5]
print(single_element_from_the_array(a))

