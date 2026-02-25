from typing import List

# Initial solution
class Solution_One:
    def missingNumber(self, nums: List[int]) -> int:
        max_num = max(nums)
        nums_set = set(nums)
        
        for num in range(max_num):
            if num not in nums_set:
                return num
        return max_num + 1
    
# O(1)-space solution
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        run = n
        for i in range(n):
            run ^= i
            run ^= nums[i]
        return run