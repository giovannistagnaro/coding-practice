from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 1:
            return 0
        elif n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        
        def robStraightStreet(new_nums):
            n = len(new_nums)
            if n < 1:
                return 0
            elif n == 1:
                return nums[0]
            elif n == 2:
                return max(new_nums[0], new_nums[1])
            
            dp = [0] * n
            dp[0], dp[1] = new_nums[0], max(new_nums[0], new_nums[1])

            for i in range(2, n):
                dp[i] = max(dp[i - 2] + new_nums[i], dp[i - 1])

            return dp[n - 1]

        return max(robStraightStreet(nums[1:]), robStraightStreet(nums[:(len(nums) - 1)]))
    