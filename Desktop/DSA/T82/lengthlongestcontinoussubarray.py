# Problem statement
# You are given ‘N’ distinct integers in the form of an array ‘ARR’. You need to print the length of the longest subarray in which the numbers are present in a continuous sequence.

# Note: All elements are distinct from the array.

# For example:
# Let ‘ARR’ be: [1, 2, 4]
# Then the largest subarray with continuous sequence will be: [1, 2]
# So the length will be 2.

def length_of_longest_ontinous_subarray(array:list[int])->int:
    
    n=len(array)
    max_len=float("-inf")
    
    def is_continous(arr:list[int])->bool:
        
        arr.sort()
        
        for i in range(1,len(arr)):
            
            if arr[i]- arr[i-1] != 1:
                
                return False
            
        
        return True
    
    for i in range(n):
        
        for j in range(i,n):
            
            substring = array[i:j+1]
            
            if is_continous(substring):
                
                max_len =max(max_len ,len(substring))
                
                
    return max_len

arr = [1, 2, 4]
print(length_of_longest_ontinous_subarray(arr))