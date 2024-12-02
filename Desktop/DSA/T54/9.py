# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def best_time_to_buy_sell_stock(array):
    
    n=len(array)
    max_profit= 0
    
    for i in range(n):
        
        for j in range(i+1,n):
            
            profit = array[j]-array[i]

            if profit > max_profit:
                
                max_profit = profit
                
    return max_profit

prices = [7, 1, 5, 3, 6, 4]
print(best_time_to_buy_sell_stock(prices))