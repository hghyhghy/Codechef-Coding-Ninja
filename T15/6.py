# longest consecutive sequence of 0 

def longest_subsequence_of_zero(array):
    
    max_length = 0
    count = 0
    
    for  i in range(len(array)):
        
        if array[i] == 0:
            
            count += 1
            
        else:
            
            max_length = max(max_length,count)
            count = 0
    
    return max_length

array = [1, 0, 0, 1, 0, 0, 0, 1, 0]
print(longest_subsequence_of_zero(array))