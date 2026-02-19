from typing import List;

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}

        for curr_str in strs:
            sorted_str = str(sorted(curr_str))
            if sorted_str in anagram_dict:
                anagram_dict[sorted_str].append(curr_str)
            else:
                anagram_dict[sorted_str] = [curr_str]

        answer = []
        for sorted_str, anagram_list in anagram_dict.items():
            answer.append(anagram_list)

        return answer