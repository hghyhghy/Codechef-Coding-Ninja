# You are given two Strings 'P' and 'Q' of equal length.



# Your task is to return 1 if String 'P' can be converted into String 'Q' by cyclically rotating it to the right any number of times ( Possibly Zero ), else return 0.



# A cyclic rotation to the right on String 'A' consists of taking String 'A' and moving the rightmost character to the leftmost position. For example, if 'A' = "pqrst", then it will be "tpqrs" after one cyclic rotation on 'A'.


def cyclically_rotated(string1,string2):
    
    concatenated= string1+string1
    
    if string2 in concatenated:
        
        return True
    
    return False

P = "pqrst"
Q = "tpqrs"

print(cyclically_rotated(P,Q))