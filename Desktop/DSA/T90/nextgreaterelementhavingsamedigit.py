# You are given a string S which represents a number. You have to find the smallest number strictly greater than the given number which contains the same set of digits as of the original number i.e the frequency of each digit from 0 to 9 should be exactly the same as in the original number.

# For example:
# If the given string is 56789, then the next greater number is 56798. Note that although 56790 is also greater than the given number it contains 1 '0' which is not in the original number and also it does not contain the digit '8'.


from itertools import permutations

def next_greater_number(number:int)->int:
    
    perm=sorted(set(["".join(p) for p in permutations(number)]))

    index=perm.index(number)

    if index+1<len(perm):
        
        return perm[index+1]
    
    else:
        
        return -1
    
s = "56789"
print(next_greater_number(s))