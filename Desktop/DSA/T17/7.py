# words do not share common letters. If no such two words exist, return 0.

def maximum_word_letter(string):
    
    def check_unique(st1,st2):
        
        return bool(set(st1)& set(st2))

    n=len(string)
    max_product=0
    
    for i in range(n):
        
        for j in range(i+1,n):
            
            if not check_unique(string[i],string[j]):
                
                product= len(words[i])* len(words[j])

                max_product = max(max_product,product)

    return max_product

    
    

words = ["abcw","baz","foo","bar","xtfn","abcdef"]
print(maximum_word_letter(words))