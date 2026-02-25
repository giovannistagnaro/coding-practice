class Solution:
    def getSum(self, a: int, b: int) -> int:
        ans = 0
        carry = 0
        for i in range(32):
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1
            
            if a_bit & b_bit == 1:
                if carry == 1:
                    ans |= 1 << i
                carry = 1
            elif a_bit ^ b_bit == 1:
                if carry != 1:
                    ans += 1 << i
            elif a_bit & b_bit == 0 and carry == 1:
                ans |= 1 << i
                carry = 0
        return ans if ans <= 0x7FFFFFFF else ~(ans ^ 0xFFFFFFFF)