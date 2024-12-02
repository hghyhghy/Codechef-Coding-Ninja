#buy and sell stock without fees

def main(array):
    
    minimum=float("inf")
    maximum=0
    
    for price in array:
        
        if price <minimum:
            
            minimum  = price
            
        profit =price-minimum
        
        if profit > maximum:
            
            maximum =profit
            
    return maximum

a=list(map(int,input().split()))
print(main(a))