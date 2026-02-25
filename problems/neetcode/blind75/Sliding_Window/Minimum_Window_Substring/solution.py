# initial solution
class Solution_One:
    def contains_sub_with_freqs(self, freq_map: dict[str, int], template_freq_map: dict[str, int]) -> bool:
        if not (set(template_freq_map.keys())).issubset(freq_map.keys()):
            return False
        
        for c in template_freq_map.keys():
            if freq_map[c] < template_freq_map[c]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''
        
        min_len = 1001  # max length of s is 1000
        min_sub = ''
        start = end = 0
        valid_chars = set(t)
        s_freq_map = {}
        t_freq_map = {}

        for c in t:
            t_freq_map[c] = 1 + t_freq_map.get(c, 0)

        while end < len(s):
            s_freq_map[s[end]] = 1 + s_freq_map.get(s[end], 0)
            if self.contains_sub_with_freqs(s_freq_map, t_freq_map):
                if (end - start) + 1 < min_len:
                    min_len = (end - start) + 1
                    min_sub = s[start:end+1]
                s_freq_map[s[start]] -= 1
                start += 1
                end = start
                s_freq_map = {}
                if start < len(s):
                    s_freq_map[s[start]] = 1
            end += 1
            if start < len(s) and s[start] not in valid_chars:
                s_freq_map[s[start]] -= 1
                start += 1
                if start > end:
                    end += 1


        return min_sub
    
# O(n)-time solution
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        start = end = 0
        t_freq_map = {}
        window_map = {}

        for c in t:
            t_freq_map[c] = 1 + t_freq_map.get(c, 0)

        chars_held, chars_needed = 0, len(t_freq_map)
        min_len = 1001
        min_sub = ''
        while end < len(s):
            curr_char = s[end]
            window_map[curr_char] = 1 + window_map.get(curr_char, 0)
            if curr_char in t_freq_map.keys() and window_map[curr_char] == t_freq_map[curr_char]:
                chars_held += 1

            while chars_held == chars_needed:
                if (end - start) + 1 < min_len:
                    min_len = (end - start) + 1
                    min_sub = s[start:end+1]

                start_char = s[start]
                window_map[start_char] -= 1
                if start_char in t_freq_map and window_map[start_char] < t_freq_map[start_char]:
                    chars_held -= 1
                start += 1

            end += 1

        return min_sub
                
solution = Solution()
print(solution.minWindow("OUZODYXAZV", "XYZ"))