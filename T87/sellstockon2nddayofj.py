# Problem statement
# You are given a list of stock prices of size 'n' called ‘prices’, where ‘prices[i]’ represents the price on ‘i’th day.



# Your task is to calculate the maximum profit you can earn by trading stocks if you can only hold one stock at a time.



# After you sell your stock on the ‘i’th day, you can only buy another stock on ‘i + 2’ th day or later.



# Example:
# Input: 'prices' = [4, 9, 0, 4, 10]

# Output: 11

# Explanation:
# You are given prices = [4, 9, 0, 4, 10]. To get maximum profits you will have to buy on day 0 and sell on day 1 to make a profit of 5, and then you have to buy on day 3  and sell on day 4 to make the total profit of 11. Hence the maximum profit is 11.

def max_profit_stock(array:list[int])->int:
    
    n=len(array)
    max_profit=float("-inf")

    for i in range(n):
        
        for j in range(i+1,n):
            
            profit=  array[j] - array[i]
            
            if profit > 0:
                
                remaining_prtofit= 0
                
                for k in range(j+2,n):
                    
                    for l in range(k+1,n):
                        
                        remaining_prtofit = max(remaining_prtofit,array[l]-array[k])

                
                max_profit = max(max_profit,remaining_prtofit+profit)

    return max_profit

prices = [3 ,7 ,7 ,1 ,3 ,8 ,4 ,4 ,8 ,10 ]
print(max_profit_stock(prices))