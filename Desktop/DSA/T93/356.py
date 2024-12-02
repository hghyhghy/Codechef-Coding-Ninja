

#distinct palindrome

def check(string:str)->bool:

    return  string.lower() == string[::-1].lower()

def main(string):

    n=len(string)
    seen=set()

    for i in range(n):

        for j in range(i,n):

            substring=string[i:j+1]

            if check(substring):

                seen.add(substring)

    return sorted(seen)

s = "abba"
print(main(s))