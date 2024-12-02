

#first repeating char

def main(string):

    freq={}

    for char in string:

        if char in freq:

            freq[char] +=1

        else:

            freq[char] =1


    for char in string:

        if freq[char] ==1:

            return  char


    return -1

s = "swiss"
print(main(s))