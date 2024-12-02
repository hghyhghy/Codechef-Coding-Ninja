# Problem statement
# You are given an array 'ARR' of the 'N' element. Your task is to find the maximum difference between any of the two elements from 'ARR'.

# If the maximum difference is even print “EVEN” without quotes. If the maximum difference is odd print “ODD” without quotes.

# For example:

# Given 'ARR' = [1, 10, 5, 2, 8, 1 ] , answer is "ODD".
# Here the maximum difference is between 10 and 1, 10 - 1 = 9

def bubble_sort(array):
    
    n=len(array)

    for i in range(n):
        
        for j in range(0,n-i-1):
            
            if array[j]<array[j+1]:
                
                array[j],array[j+1]=array[j+1],array[j]

    return array

def main(array):
    
    temp=bubble_sort(array)
    minimum = temp[len(temp)-1]

    return temp[0]-minimum

a= [1, 10, 5, 2, 8, 1 ]
print(main(a))