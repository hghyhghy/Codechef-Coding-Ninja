# Problem statement
# You have been given an array/list 'ARR' consisting of 'N' integers. Your task is to find the majority element in the array. If there is no majority element present, print -1.

# Note:
# A majority element is an element that occurs more than floor('N' / 2) times in the array.

def majority_element(arr):
    
    freq={}

    for num in arr:
        
        if num  in freq:
            
            freq[num] += 1
            
        else:
            
            freq[num]  = 1
            
    
    result = [num for num,count in freq.items() if count > 1]

    return result

a=[2 ,3 ,9 ,2 ,2]
print(majority_element(a))