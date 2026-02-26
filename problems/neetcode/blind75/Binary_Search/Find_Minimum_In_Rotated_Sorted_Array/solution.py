from typing import List

class Solution:
    def binarySearch(self, nums: List[int], start: int, end: int, mid: int) -> int:
        if nums[mid] <= nums[mid - 1]:
            return nums[mid]
        
        if (end - start == 1):
            return nums[end] if nums[end] < nums[start] else nums[start]

        if nums[start] > nums[mid]:
            return self.binarySearch(nums, start, mid, (start + mid) // 2)
        elif nums[end] < nums[mid]:
            return self.binarySearch(nums, mid, end, (mid + end) // 2)
        else:
            return nums[start]

    def search(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return self.binarySearch(nums, 0, len(nums) - 1, (len(nums) - 1) // 2)