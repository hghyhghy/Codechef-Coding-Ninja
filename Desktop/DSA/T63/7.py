# Problem statement
# You have been given an integer array/list(ARR) of size 'N'. It only contains 0s, 1s and 2s. Write a solution to sort this array/list.

# Note :
# Try to solve the problem in 'Single Scan'. ' Single Scan' refers to iterating over the array/list just once or to put it in other words, you will be visiting each element in the array/list just once.

def sorting(array):
    
    low=0
    mid=0
    hight=len(array) - 1
    
    while mid<=hight:
        
        if array[mid] == 0:
            
            array[low],array[mid]=array[mid],array[low]
            
            low += 1
            mid += 1
            
        elif array[mid] == 1:
            
            mid += 1
            
            
        else:
            
            array[mid],array[hight]=array[hight],array[mid]
            hight -= 1
            
    return arr

arr = [2, 0, 2, 1, 1, 0]
print(sorting(arr))