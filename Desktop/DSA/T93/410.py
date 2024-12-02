

#count vowel in substring

def main(string):

    vowels = {'a', 'e', 'i', 'o', 'u'}
    n=len(string)
    count = 0

    for i in range(n):

        for j in range(i,n):

            if string[j] in vowels:

                count +=1

            else:

                break

    return  count

s = "aeioubc"
print(main(s))