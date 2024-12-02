# You are given an array/list 'prices' where the elements of the array represent the prices of the stock as they were yesterday and indices of the array represent minutes. Your task is to find and return the maximum profit you can make by buying and selling the stock. You can buy and sell the stock only once.

def best_time_to_buy_sell_stock(array):
    
    max_profit= float("-inf")
    minimm_price= float("inf")
    
    for num in array:
        
        if num < minimm_price:
            
            minimm_price = num
            
        profit  =  num-minimm_price
        
        if profit> max_profit:
            
            max_profit = profit
            
    return max_profit

a=[ 2, 100, 150, 120]
print(best_time_to_buy_sell_stock(a))