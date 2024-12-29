class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowPrice = prices[0]
        maxProfit = 0
        for p in prices[1:]:
            if lowPrice > p:
                lowPrice = p
            else:
                maxProfit = max(maxProfit, p - lowPrice)
        return maxProfit
