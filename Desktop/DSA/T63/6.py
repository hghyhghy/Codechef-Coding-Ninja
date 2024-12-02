# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

# Find and return the maximum profit you can achieve.

def best_time_to_buy_sell_stock(array):
    
    maximum=0
    
    for i in range(1,len(array)):
        
        if array[i] > array[i-1]:
            
            maximum += array[i]-array[i-1]

    return maximum

prices = [7, 1, 5, 3, 6, 4]
print(best_time_to_buy_sell_stock(prices))
    

    

