

#top k frequent elemnt s

def main(string,k):

    n=len(string)
    maximum=float('-inf')

    for i in range(n):

        freq={}

        for j in range(i,n):

            char =  string[j]

            if char in freq:

                freq[char]+=1

            else:

                freq[char]=1


            if all(count >= k for count in freq.values()):

                maximum=max(maximum,j-i+1)

    return  maximum

s = "aaabb"
k = 3
print(main(s,k))