# Problem statement
# You are given an array/list 'ARR' of integers of length ‘N’. You are supposed to find all the elements that occur strictly more than floor(N/3) times in the given array/list.

def majority_element_from_array(array):
    
    freq={}

    for num in array:
        
        if num in freq:
            
            freq[num] += 1
            
        else:
            
            freq[num] = 1
            
    result=[num for num,count in freq.items() if count > 1]

    return result

a=[3 ,2 ,2 ,1 ,5 ,2 ,3]
print(majority_element_from_array(a))