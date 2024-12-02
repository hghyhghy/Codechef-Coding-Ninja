
#distinct substring

def main(string):

    n=len(string)
    seen=set()

    for  i in range(n):

        for j in range(i+1,n+1):

            substring = string[i:j]

            seen.add(substring)

    return  len(seen)+1

S = "abc"
print(main(S))
