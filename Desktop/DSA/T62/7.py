# You are given an array of size ‘N’. The elements of the array are in the range from 1 to ‘N’.

# Ideally, the array should contain elements from 1 to ‘N’. But due to some miscalculations, there is a number R in the range [1, N] which appears in the array twice and another number M in the range [1, N] which is missing from the array.

# Your task is to find the missing number (M) and the repeating number (R).

# For example:
# Consider an array of size six. The elements of the array are { 6, 4, 3, 5, 5, 1 }. 
# The array should contain elements from one to six. Here, 2 is not present and 5 is occurring twice. Thus, 2 is the missing number (M) and 5 is the repeating number (R). 

def main(array):

    def missing_number(array):
        
        n=len(array)
        expected_sum = n*(n+1)//2
        
        actual =  sum(array)

        missing =  expected_sum -  actual
        
        return missing
    
    def repeatative(array):
        
        freq={}

        for num in array:
            
            if num in freq:
                
                freq[num] += 1
                
            else:
                
                freq[num] = 1
                
                
        result=[num for num,count in freq.items() if count > 1 ]

        return result
    
    missing= missing_number(array)
    duplicate=repeatative(array)

    return missing,duplicate

arr = [1, 2, 2, 4, 5]
print(main(arr))
