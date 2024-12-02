# You have been given the prices of 'N' stocks in an array where each array element represents the stock price for that day. You need to find the maximum profit which you can make by buying and selling the stocks. You may make as many transactions as you want but can not have more than one transaction at a time i.e, if you have the stock, you need to sell it first, and then only you can buy it again.

def buy_and_sell_stock(array:list[int])->int:
    
    n=len(array)
    max_profit = 0
    
    for i in range(1,n):
        
        if array[i]>array[i-1]:
            
            max_profit += array[i]-array[i-1]
            
    return max_profit

prices = [7, 1, 5, 3, 6, 4]
print(buy_and_sell_stock(prices))