import random
from collections import defaultdict

class RandomizedCollection:

    def __init__(self):
        self.val_to_idx_map = defaultdict(set)
        self.values = []

    def insert(self, val: int) -> bool:
        current_set = self.val_to_idx_map[val]
        current_values = self.values

        current_set.add(len(current_values))
        current_values.append(val)

        return len(current_set) == 1

    def remove(self, val: int) -> bool:
        current_set = self.val_to_idx_map[val]
        current_values = self.values

        if not current_set:
            return False

        idx = current_set.pop()
        last = current_values[-1]

        current_values[idx] = last
        self.val_to_idx_map[last].add(idx)
        self.val_to_idx_map[last].discard(len(current_values) - 1)

        current_values.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)
