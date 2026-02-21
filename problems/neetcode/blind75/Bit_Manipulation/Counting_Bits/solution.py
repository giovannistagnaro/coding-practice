from typing import List

# First solution
class Solution_One:
    def hammingWeight(self, n: int) -> int:
        num_zeros = 0
        while (n != 0):
            if (n & 1) % 2 == 1:
                num_zeros += 1
            n >>= 1
        return num_zeros
    
    def countBits(self, n: int) -> List[int]:
        num_bits = [0] * (n + 1)
        for i in range(n + 1):
            num_bits[i] = self.hammingWeight(i)
        return num_bits
    
# Combined to one function
class Solution:
    def countBits(self, n: int) -> List[int]:
        num_bits = [0] * (n + 1)
        for i in range(n + 1):
            num_bits[i] = num_bits[i >> 1] + (i & 1)
        return num_bits