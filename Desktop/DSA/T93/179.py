

#best time to buy and sell stock

def main(array):
    
    minimum=array[0]
    max_profit=0
    
    for num in array:
        
        minimum = min(minimum,num)

        profit=num-minimum
        
        max_profit=max(max_profit,profit)

    return max_profit

prices = [7, 1, 5, 3, 6, 4]
print(main(prices))