

#reverse words 

def main(string):
    
    words=string.split()

    reversd_word=[word[::-1] for word in words]

    return ''.join(reversd_word)

s = "Hello World"
print(main(s))