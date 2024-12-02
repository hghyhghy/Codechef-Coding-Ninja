# Problem statement
# You are given a string ‘str’ of size ‘N’. Your task is to remove consecutive duplicates from this string recursively.

# For example:

# If the input string is ‘str’ = ”aazbbby”, then your output will be “azby”.
# Note that we are just removing adjacent duplicates.


def main(string:str)->str:

    if len(string) == 0:

       return "" 

    result=string[0]
    for i in range(1,len(string)):

        if string[i] != string[i-1]:

           result += string[i]

    return result

print(main("aazbbby"))
