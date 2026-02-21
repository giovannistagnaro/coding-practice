class Solution:
    def hammingWeight(self, n: int) -> int:
        num_zeros = 0
        while (n != 0):
            if (n & 1) % 2 == 1:
                num_zeros += 1
            n >>= 1
        return num_zeros