#remove duplicates


def main(string):

    n=len(string)
    result=string[0]

    for i in range(1,n):


        if string[i] != string[i-1]:

            result += string[i]

    return  "".join(result)


STR = "aabbccddeeeffggh"
print(main(STR))