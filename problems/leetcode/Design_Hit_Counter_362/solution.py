from bisect import bisect_left
from collections import defaultdict, deque

class HitCounterSolutionOne:
    def __init__ (self):
        self.hit_map = defaultdict(int)

    def hit(self, timestamp):
        self.hit_map[timestamp] += 1

    def getHits(self, timestamp):
        total_hits = 0
        for i in range(max(timestamp - 299, 0), timestamp + 1, 1):
            total_hits += self.hit_map[i]

        return total_hits
    
class HitCounter:
    def __init__ (self):
        self.hits = []

    def hit(self, timestamp):
        self.hits.append(timestamp)

    def getHits(self, timestamp):
        l = timestamp - 300 + 1
        first_valid = bisect_left(self.hits, l)

        return len(self.hits) - first_valid