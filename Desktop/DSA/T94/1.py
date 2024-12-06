
#first repeatitive charater

def main(string):

    freq={}
    order=[]

    for  num in  string:

        if num in freq:

            freq[num]+=1

        else:

            freq[num] =1
            order.append(num)


    for char in order:

        if freq[char] > 1:

            return  char


    return  -1;

STR = "abccba"
print(main(STR))

