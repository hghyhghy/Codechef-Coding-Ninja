# first n fionacci numbers 

def first_n_fibonacci_number(n):
    
    store=[]

    if n <=0 :
        
        return store
    
    a=0
    b=1
    
    for _ in range(n):
        
        store.append(a)
        a,b=b,a+b

    return store

n=10
print(first_n_fibonacci_number(n))