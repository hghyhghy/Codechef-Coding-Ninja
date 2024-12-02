#
#
# #4.	Print all the duplicate characters in a string
# Input: “WelcometoCodelogicx”
# Expected Output :
# e , count = 3
# l , count =2
# c , count = 2
# o , count = 4


def finding_duplictes(string:str):

    freq={}

    for char in string:

        freq[char] = freq.get(char,0)+1


    for char,count in freq.items():

        if count > 1:

            print(f"{char},count={count}")


    return  -1


input_string = "WelcometoCodelogicx"
print(finding_duplictes(input_string))