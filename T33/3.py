# Ninja loves playing with numbers. So his friend gives him an array on his birthday. The array consists of positive and negative integers. Now Ninja is interested in finding the length of the longest subarray whose sum is zero.

def largest_subarray_with_zero_sum(array):
    
    n=len(array)

    lenght=0
    index=-1
    
    for start in range(n):
        
        current_sum= 0
        
        for end in range(start,n):
            
            current_sum += array[end]

            if current_sum == 0:
                
                custom_lenght= end-start+1
                
                lenght = max(lenght,custom_lenght)
                index = start

    return lenght,index

arr = [1, 2, -3, 4, -2, -1, 5, -4, 2]
print(largest_subarray_with_zero_sum(arr))