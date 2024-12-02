

#first repeatitive char


def func(string):

    freq={}
    order=[]

    for char in string:

        if char in freq:

            freq[char] +=1

        else:

            freq[char] =1
            order.append(char)


    for char in order:

        if freq[char] > 1:


            return  char

    return  None

STR = "abccba"
print(func(STR))

