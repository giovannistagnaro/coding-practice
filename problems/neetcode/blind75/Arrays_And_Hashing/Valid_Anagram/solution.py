from collections import defaultdict

class Solution_First:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sorted = sorted(s)
        t_sorted = sorted(t)

        if len(s_sorted) == len(t_sorted):
            for i in range(len(s_sorted)):
                if s_sorted[i] != t_sorted[i]:
                    return False
            return True
        return False

# Hash map instead of sorting for lower time complexity
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freqs = defaultdict(int)
        for c in s:
            s_freqs[c] += 1

        for c in t:
            s_freqs[c] -= 1

        for freq in s_freqs.values():
            if freq != 0:
                return False
        return True