
# you have been given a string having space separated with multiple characters ,replrint the word after deleeting all the char that appear
# more than once in the string 


def deleting_duplicates(string):

    words=string.split()

    store=[]

    for word in words:

        frequency={}

        for  char in word:

            if char in frequency:

                frequency[char] += 1

            else:

                frequency[char] = 1

     
        filtered_word="".join([char for char in word if frequency[char] == 1])

        store.append(filtered_word)

    return " ".join(store)


a="apple banana cherry"
print(deleting_duplicates(a))