from collections import defaultdict
from typing import List


class Solution:

    """
    Iterates through each element of the input list, keeping track of the complement 
    required to reach the target sum.
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        complement_map = defaultdict(int)

        for i in range(len(nums)):
            num = nums[i]
            complement = target - num

            if complement in complement_map:
                return [complement_map[complement], i]
            
            complement_map[num] = i
        
        return []