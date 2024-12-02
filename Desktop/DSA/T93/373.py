

#removal of vowel

def main(string):

    vowel = "aeiouAEIOU"
    result=[]

    for char in string:

        if char in vowel:

            continue

        result.append(char)

    return  result

STR1 = 'CodeGeek'
print(main(STR1))