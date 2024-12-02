# Problem statement
# You are given an array of integers, 'PRICES' of size 'N', where 'PRICES[i]' is the price of a given stock on 'i'th day.

# On each day, you may decide to buy and sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it and then immediately sell it on the same day.

# Return the maximum profit you can achieve.

# Note: You can't sell a stock before you buy one.

# Example:
# Let's say, 'PRICES' = [7, 1, 5, 4, 3, 6]

# Purchase stock on day two, where the price is one, and sell it on day three, where the price is five, profit = 5 - 1 = 4.
# Purchase stock on day five, where the price is three, and sell it on day six, where the price is six, profit = 6 - 3 = 3.
# Total Profit is 4+3 = 7. Hence we return 7.

def best_time_to_buy_sell_stock(array:list[int])->int:
    
    n=len(array)
    max_profit= 0
    
    for i  in range(n-1):
        
        if array[i+1]>array[i]:
            
            max_profit += array[i+1] - array[i]
            
    return max_profit

PRICES = [7, 1, 5, 4, 3, 6]
print(best_time_to_buy_sell_stock(PRICES))