
# Implement the following functions.a

# char*MoveHyphen(char str[],int n);

# The function accepts a string “str” of length ‘n’, that contains alphabets and hyphens (-). Implement the function to move all hyphens(-) in the string to the front of the given string.

# NOTE:- Return null if str is null.

def moving_hyphen(string):

    if not string:

        return None
    
    index=0
    result=[]

    for char in string:

        if char == "-":

            

            index += 1

        else:

            result.append(char)

    return "-"*index+"".join(result)

s = "ab-c-d-ef"
print(moving_hyphen(s))

