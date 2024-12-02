# Problem statement
# You are given an array of integers 'prices' of size 'n', where ‘prices[i]’ is the price of a given stock on an ‘i’-th day. You want to maximize the profit by choosing a single day to buy one stock and a different day to sell that stock.



# Please note that you can’t sell a stock before you buy one.

def buy_and_sell_stock(prices:list[int])->int:
    
    minimum  = float("inf")
    maximum = 0 
    
    
    for price in prices:
        
        if price < minimum:
            
            minimum  = price
            
        profit  = price - minimum
        
        if profit > maximum:
            
            maximum =  profit
            
    return maximum

