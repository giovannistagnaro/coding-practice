from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start, end = 0, 0
        max_profit = 0

        while end < len(prices):
            current_profit = prices[end] - prices[start]
            max_profit = max(current_profit, max_profit)
            if prices[start] > prices[end]:
                start = end
            end += 1

        return max_profit
    
solution = Solution()
print(solution.maxProfit([10,8,7,5,2]))