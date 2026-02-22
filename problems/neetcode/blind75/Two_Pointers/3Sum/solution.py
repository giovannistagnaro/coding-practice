from typing import List

# First attempt
class Solution_One:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sums = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums), 1):
                for k in range(j + 1, len(nums), 1):
                    if nums[i] + nums[j] + nums[k] == 0:
                        sorted_sum = sorted([nums[i], nums[j], nums[k]])
                        if sorted_sum not in sums:
                            sums.append(sorted_sum)
                        
        return sums

# two-pointer solution
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sums = []
        sorted_nums = sorted(nums)
        for left, curr_left in enumerate(sorted_nums):
            for right, curr_right in enumerate(sorted_nums[left + 1:], start=left + 1):
                third_num = 0 - (curr_left + curr_right)
                candidate_sum = [curr_left, curr_right, third_num]
                if third_num in sorted_nums[right + 1:] and candidate_sum not in sums:
                    sums.append(candidate_sum)
        return sums