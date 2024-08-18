# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


def max_time_to_but_sell_stock(array):
    
    n=len(array)
    net_profit = 0
    for start in range(n):
           
        
        for end in range(start+1,n):
            
            max_profit = array[end] - array[start]

            net_profit =max(net_profit,max_profit)

    return net_profit

prices = [7, 1, 5, 3, 6, 4]
print(max_time_to_but_sell_stock(prices))
