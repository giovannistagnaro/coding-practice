from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        grouped_anagrams = []

        for string in strs:
            sorted_str = ''.join(sorted(string))
            anagrams[sorted_str].append(string)

        for bucket in anagrams.values():
            grouped_anagrams.append(bucket)

        return grouped_anagrams