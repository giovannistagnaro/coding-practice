from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(heights) - 1

        while right > left:
            curr_left, curr_right = heights[left], heights[right]
            curr_area = min(heights[left], heights[right]) * (right - left)
            max_area = max(max_area, curr_area)
            if curr_left > curr_right:
                right -= 1
            else:
                left += 1
        return max_area