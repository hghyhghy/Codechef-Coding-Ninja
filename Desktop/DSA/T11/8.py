# Write a program to print all the combinations of the given word with or without meaning (when unique characters are given).

from itertools import combinations

def combination(words):
    
    n=len(words)
    result=[]

    for i in range(1,n+1):
        
        for combo in combinations(words,i):
            
            result.append("".join(combo))

    
    return result

word=input("Enter a word")

combinations_list = combination(word)
for combo in combinations_list:
    print(combo)