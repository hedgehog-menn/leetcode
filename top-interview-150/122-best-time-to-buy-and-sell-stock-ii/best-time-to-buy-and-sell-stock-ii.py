class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Sell imdiedately when profit == max profit
        profit = 0
        """
        buyPrice = prices[0]
        for currentPrice in prices:
            if currentPrice < buyPrice:
                buyPrice = currentPrice
            else:
                profit += currentPrice - buyPrice
                buyPrice = currentPrice
        """

        for i in range(1, len(prices)):
            if prices[i - 1] < prices[i]:
                profit += prices[i] - prices[i - 1]

        return profit
                

            
        