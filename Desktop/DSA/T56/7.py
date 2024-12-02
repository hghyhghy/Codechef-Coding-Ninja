# Alice has two numbers, 'X' and 'Y'. He is asked to perform the following operations any number of times.

# Alice adds 1 to 'X' if 'X' is odd. Alice adds 2 to 'X' if 'X' is even. Will he be able to make 'X' equal to 'Y'?



# Return 1 if 'X' can be made equal to 'Y' using the above operations any number of times(possibly 0) and 0 otherwise.

# Note: Assume 1-based indexing.

def can_make_equal(x,y):
    
    if not x or not y:
        
        return "NO"

    
    if x<=y and (x%2) == (y%2):
        
        return 1
    
    else:
        
        return 0
    
print(can_make_equal(5, 11))