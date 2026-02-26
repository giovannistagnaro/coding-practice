from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.key_value_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_value_map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_value_map.keys():
            return ""
        values = self.key_value_map[key]

        l, r = 0, len(values) - 1

        while l < r:
            mid = (l + r) // 2
            if values[mid][1] < timestamp:
                l = mid + 1
            else:
                r = mid

        if values[r][1] <= timestamp:
            return values[r][0]
        elif r - 1 >= 0:   
            return values[r-1][0]
        else:
            return ""