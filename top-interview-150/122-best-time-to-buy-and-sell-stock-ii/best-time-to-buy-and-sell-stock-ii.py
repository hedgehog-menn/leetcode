class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Sell imdiedately when profit == max profit
        profit = 0
        buyPrice = prices[0]
        for currentPrice in prices:
            if currentPrice < buyPrice:
                buyPrice = currentPrice
            else:
                profit += currentPrice - buyPrice
                buyPrice = currentPrice
        return profit
                

            
        