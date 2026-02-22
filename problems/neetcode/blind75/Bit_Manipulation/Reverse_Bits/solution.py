# Brute force
class Solution:
    def reverseBits(self, n: int) -> int:
        bits = bin(n)[2:]   # remove 0b from beginning
        rev_bits = [0] * 32
        for i in range(len(bits) - 1, -1, -1):
            rev_bits[len(bits) - 1 - i] = bits[i]
        return int("".join(map(str, rev_bits)), 2)
    
# Slightly better
class Solution:
    def reverseBits(self, n: int) -> int:
        rev_bits = 0

        for i in range(32):
            curr_bit = (n >> i) & 1
            rev_bits += (curr_bit << (31 - i))

        return rev_bits