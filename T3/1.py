# Given an integer array and an integer element, count the number of occurrences of the element in the array.

def finding_frequency(array,num):
    
    count = 0
    
    for i in range(len(array)):
        
        if array[i] == num:
            
            count += 1
            
    return count

arr=[5, 2, 4, 1, 2]
num=2
print(finding_frequency(arr,num))