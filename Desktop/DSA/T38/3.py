# Problem statement
# Take an array with N elements with possibly duplicate elements as the input. The task is to find the index of the last occurrences of the element x in the array and, if it is not present, return -1.

def last_occurance_of_the_element(array,target):
    
    last_index=-1
    
    for i in range(len(array)):
        
        if array[i] == target:
            
            last_index = i
    
    return last_index


arr = [1, 2, 3, 4, 2, 5, 2, 6]
x = 2
print(last_occurance_of_the_element(arr,x))