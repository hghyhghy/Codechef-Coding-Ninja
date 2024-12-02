# Problem statement
# You are given an array/list 'ARR' consisting of N integers, which contains elements only in the range 0 to N - 1. Some of the elements may be repeated in 'ARR'. Your task is to find all such duplicate elements.

# Note:
# 1. All the elements are in the range 0 to N - 1.
# 2. The elements may not be in sorted order.
# 3. You can return the duplicate elements in any order.
# 4. If there are no duplicates present then return an empty array.

def find_duplicates_in_the_array(array):
    
    freq={}
    for num in array:
        
        if num in freq:
            freq[num] += 1
            
        else:
            freq[num] = 1
            
    
    result=[num for num,count in freq.items() if count > 1]
    
    return result

a=[3, 2 ,1, 3 ,2, 1, 5]
print(find_duplicates_in_the_array(a))