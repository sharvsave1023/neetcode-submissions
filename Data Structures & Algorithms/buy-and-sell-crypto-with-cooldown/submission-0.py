from functools import lru_cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # array of prices, if last was bought, must skip current

        # maximize profit so
            # max(some path, some other path)

        self.prices = prices

        return self.dp( False, 0)


    # have it be max profit you can get from holding or selling on ith day 
    @lru_cache(None)
    def dp(self, holding, i):
        #last day
        if i >= len(self.prices):
            return 0
        maxProfit = self.dp(holding, i+1)
        if holding:
            maxProfit = max(maxProfit, self.dp(not holding, i + 2) + self.prices[i])
        else:
            maxProfit = max(maxProfit, self.dp(not holding, i + 1) - self.prices[i])
        return maxProfit
            