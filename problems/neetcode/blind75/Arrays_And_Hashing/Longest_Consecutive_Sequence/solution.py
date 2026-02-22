from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> List[int]:
        num_set = set(nums)
        max_size = 0
        curr_size = 0
    
        for i in range(len(nums)):
            curr_num = nums[i]
            if curr_num in num_set:
                while curr_num - 1 in num_set:
                    curr_num -= 1
                while curr_num in num_set:
                    num_set.remove(curr_num)
                    curr_num += 1
                    curr_size += 1
                    if curr_size > max_size:
                        max_size = curr_size
                curr_size = 0
                    
        return max_size
