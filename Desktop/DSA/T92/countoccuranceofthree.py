# Problem statement
# You are given an integer ‘N’. You simply need to find out the number of occurrences of 3 as a digit in the range of numbers from [0, N].

# Note:
#  You need to count occurrences at every place of the number.
# For example :
# You are given N = 13, then the number of occurrences of 3 in range [0, 13] = 2 (3, 13), you need to return 2.

def count_no_of_occurance_of_three(n:int)->int:
    
    count = 0
    
    for  i in range(n+1):
        
        count += str(i).count("3")

    return count

N = 13
print(count_no_of_occurance_of_three(N))