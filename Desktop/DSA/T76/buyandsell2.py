# You have been given stock values/prices for N number of days. Every i-th day signifies the price of a stock on that day. Your task is to find the maximum profit which you can make by buying and selling the stocks.

#  Note :
# You may make as many transactions as you want but can not have more than one transaction at a time i.e, if you have the stock, you need to sell it first, and then only you can buy it again.
# Detailed explanation ( Input/output form

def buy_and_sell_stock_II(array:list[int])->int:
    
    max_profit=0
    n=len(array)
    
    for i in range(1,n):
        
        if array[i]>array[i-1]:
            
            max_profit += array[i] - array[i-1]
            
    return max_profit

prices = [7, 1, 5, 3, 6, 4] 
print(buy_and_sell_stock_II(prices))