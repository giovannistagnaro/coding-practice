from typing import List

# naive solution O(n^2)
class Solution_One:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1] * len(nums)
        for i in range(len(nums)):
            num = nums[i]
            for j in range(len(nums)):
                if j == i:
                    continue
                products[i] *= nums[j]
        return products
    
# better solution using prefix/suffix multiplication
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            products[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            products[i] *= suffix
            suffix *= nums[i]
            
        return products