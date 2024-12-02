
#removing duplicates


def main(array):

    seen=set()
    r=[]

    for char in array:

        if char not in seen:

            seen.add(char)
            r.append(char)


    return  "".join(r)

a="abcadeecfb"
print(main(a))

