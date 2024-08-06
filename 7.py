# Find the Majority Element that occurs more than N/2 times


# 191

# 0
# Problem Statement: Given an array of N integers, write a program to return an element that occurs more than N/2 times in the given array. You may consider that

def majority_element(array):
    
    frequency={}
    n=len(array)

    for num in array:
        
        if num  in frequency:
            
            frequency[num] += 1
            
        else:
            
            frequency[num] = 1
            
            
    for num,count in frequency.items():
        
        if count > n//2:
            
            return num
        
    return None

arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]
print(majority_element(arr))