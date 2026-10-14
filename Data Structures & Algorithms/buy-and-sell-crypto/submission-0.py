class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sol = 0
        low = prices[0]
        for day in prices: 
            if day < low:
                low = day
            sol = max(sol, day - low)
        return sol