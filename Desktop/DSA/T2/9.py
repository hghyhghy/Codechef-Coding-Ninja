# Given an array of integers, find the average of all positive numbers in the array.

def finding_average_of_all_integers(array):
    
    count=0
    sum = 0
    for i in range(len(array)):
        
        if array[i] > 0:
            
            sum += array[i]
            count += 1
            
    
    return sum % count


a=[5, 2, -4, 1, 3]
print(finding_average_of_all_integers(a))