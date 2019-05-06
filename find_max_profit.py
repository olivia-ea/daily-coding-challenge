"""
array each element is price of stock on that day

[100, 101, 102] => 2 

[7,1,5,3,6,4] => 5 (buy on day 2 = price is $1, sell on day 5= price is $6) 6-1=5

[7,6,4,3,1] => answer is 0 because the stock price only kept decreasing, it never went up, so no matter what day you bought it on, selling it would result in loss

[3, 7, 2, 1, 6] => 5



"""

def find_max_profit(lst):
    min_price = max(lst)
    max_profit = 0
    
    for num in lst:
        if num < min_price:    
            min_price = num
        elif max_profit < num - min_price:
            max_profit = num - min_price
            
    return max_profit
    