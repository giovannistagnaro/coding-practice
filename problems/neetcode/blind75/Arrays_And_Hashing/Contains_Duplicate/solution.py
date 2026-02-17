from typing import List
from collections import defaultdict

# first iteration
class Solution_First:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup_map = defaultdict(lambda: False)
        for num in nums:
            if dup_map[num]:
                return True
            else:
                dup_map[num] = True
        
        return False
    
# second iteration; realized a set makes more sense
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup_set = set()
        for num in nums:
            if num in dup_set:
                return True
            else:
                dup_set.add(num)
        return False