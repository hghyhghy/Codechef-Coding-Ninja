# best time to buy and sell stock

def best_time_to_buy_and_sell_stock(array):
    
    if not array:
        
        return None
    
    minimum = array[0]
    max_profit = 0
    
    for num in array:
        
        minimum=min(minimum,num)

        profit   = num - minimum
        
        max_profit = max(max_profit,profit)

    return max_profit

prices = [7, 1, 5, 3, 6, 4]
print(best_time_to_buy_and_sell_stock(prices))