# # You are given an array/list 'prices' where the elements of the array represent the prices of the stock as they were yesterday and indices of the array represent minutes. Your task is to find and return the maximum profit you can make by buying and selling the stock. You can buy and sell the stock only once.

# Note:

# using dynamic programming

def buy_stock_using_DP(array):
    
    n=len(array)
    minimum = array[0]

    dp=[0]*n
    
    for i in range(1,n):
        
        minimum = min(minimum,array[i])

        dp[i] = array[i] - minimum
        
    return max(dp)

prices = [7, 1, 5, 3, 6, 4]
print(buy_stock_using_DP(prices))