class Solution:
    def longestPalindrome(self, s: str) -> str:
        max, max_len = '', 0
        n = len(s)

        def expand(left, right):
            nonlocal max, max_len, s
            while left >= 0 and right < n and s[left] == s[right]:
                curr_len = right - left + 1
                if curr_len > max_len:
                    max_len = curr_len
                    max = s[left:right+1]
                left, right = left - 1, right + 1

        for i in range(n):
            expand(i, i)
            expand(i, i + 1)

        return max