import random

class RandomizedSet():
    def __init__(self):
        self.value_list = []
        self.val_to_idx_map = {}

    def insert(self, val):
        if val in self.val_to_idx_map:
            return False
        self.val_to_idx_map[val] = len(self.value_list)
        self.value_list.append(val)
        return True

    def remove(self, val):
        if val not in self.val_to_idx_map:
            return False
        
        idx = self.val_to_idx_map[val]
        self.value_list[idx] = self.value_list[-1]
        self.val_to_idx_map[self.value_list[-1]] = idx
        self.value_list.pop()
        del self.val_to_idx_map[val]
        return True

    def getRandom(self):
        return random.choice(self.value_list)