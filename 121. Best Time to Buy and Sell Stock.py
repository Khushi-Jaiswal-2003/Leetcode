prices = [1,2]
min_price=prices[0]
profit = 0
for i in range(len(prices)):
    if prices[i]<min_price:
        min_price=prices[i]
    elif prices[i]-min_price>profit:
        profit=prices[i]-min_price
print(profit)