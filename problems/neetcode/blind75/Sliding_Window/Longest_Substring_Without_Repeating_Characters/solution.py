class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        repeat_set = set()
        max_size = 0

        while end < len(s):
            while s[end] in repeat_set:
                repeat_set.discard(s[start])
                start += 1
            max_size = max(max_size, end - start + 1)
            repeat_set.add(s[end])
            end += 1

        return max_size

solution = Solution()
print(solution.lengthOfLongestSubstring("xxxx"))
        