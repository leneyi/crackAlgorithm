
def maxProfit(prices):
    if len(prices) ==0:
        return 0;
    minPrice = max(prices);
    maxValue = 0;
    for i in range(len(prices)):
       minPrice = min(minPrices, prices[i]);
       maxValue = max(maxValue, prices[i]-minPrices);
    return maxValue;
