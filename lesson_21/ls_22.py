def tradet(prices):
    for i in range(len(prices) - 1):
        if prices.index(min(prices)) < prices.index(max(prices)):
            return max(prices) - min(prices)
        else:
            prices.pop(prices.index(max(prices)))
    for j in range(len(prices)):
        return min(prices) - max(prices)


prices = [7, 1, 4, 3, 6, 4]   #выход: 8
# prices = [5,2,1,1,1]   #выход: 0
print(tradet(prices))