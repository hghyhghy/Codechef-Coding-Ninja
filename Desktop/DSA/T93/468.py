

#consecutive dupli

def main(string):

    n=len(string)
    r=string[0]

    for i in range(1,n):

        if string[i] != string[i-1]:

            r += string[i]

    return r

print(main("aazbbby"))
