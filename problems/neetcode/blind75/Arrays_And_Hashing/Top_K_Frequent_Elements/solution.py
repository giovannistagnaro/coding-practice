import heapq
from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_map = {}
        max_heap = []

        for num in nums:
            if num not in freq_map:
                freq_map[num] = 0
            freq_map[num] += 1
        
        for num, frq in freq_map.items():
            heapq.heappush(max_heap, [-frq, num])

        answer = []
        for i in range(k):
            answer.append((heapq.heappop(max_heap))[1])

        return answer
    