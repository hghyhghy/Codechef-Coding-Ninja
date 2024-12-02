

# Given a string array words, return the maximum value of the product of the length of the words 

def has_common(w1,w2):
    
    set1=set(w1)
    set2=set(w2)

    return set1.isdisjoint(set2)

def max_product(string):
    
    n=len(string)
    max_product=0
    
    for i in range(n):
        
        for j in range(i+1,n):
            
            if has_common(string[i],string[j]):
                
                lenght=len(string[i])*len(string[j])
                
                max_product=max(max_product,lenght)

    return max_product

words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
print(max_product(words))