class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        chars = set(s)
        
        for character in chars:
            start = end = 0
            num_non_target_chars = 0
            while end < len(s):
                if s[end] != character:
                    num_non_target_chars += 1
                    if num_non_target_chars > k:
                        start = end = start + 1
                        num_non_target_chars = 0
                        continue
                max_length = max(max_length, end - start + 1)
                end += 1
        
        return max_length