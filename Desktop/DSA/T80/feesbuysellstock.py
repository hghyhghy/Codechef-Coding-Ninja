# Problem statement
# You are given an array 'prices' of size 'n', denoting the price of stocks on 'n' days.



# Rahul can buy one stock at a time, and he must sell it before buying stock on another day.



# The entire transaction of selling and buying the stock requires some transaction fee, given as 'fee'.



# Find the maximum profit Rahul can achieve by trading on the stocks.

def best_time_to_buy_sell_stock(prices:list[int],fee:int)->int:
    
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        # Update minimum price
        min_price = min(min_price, price)
        
        # Calculate potential profit for current day
        profit = (price - min_price) + fee
        
        # Update maximum profit
        if profit > max_profit:
            max_profit = profit

    return max_profit

prices1 = [3, 4, 5, 63, 3, 6]
fee1 = 1
print(best_time_to_buy_sell_stock(prices1,fee1))