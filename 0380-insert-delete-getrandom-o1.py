import random

class RandomizedSet:
    """Data structure that supports insert, remove, and getRandom in average O(1) time.

    All operations work in average O(1) time complexity.
    """

    def __init__(self):
        # Your implementation here
        self.elements = []
        self.element_to_idx = {}
        pass

    def insert(self, val: int) -> bool:
        # Your implementation here
        if val in self.element_to_idx:
            return False
        self.elements.append(val)
        self.element_to_idx[val] = len(self.elements) - 1
        return True

    def remove(self, val: int) -> bool:
        # Your implementation here
        if val not in self.element_to_idx:
            return False
        self.element_to_idx[self.elements[-1]] = self.element_to_idx[val]
        self.elements[self.element_to_idx[val]] = self.elements[-1]
        
        del self.element_to_idx[val]
        self.elements.pop()
        return True

    def getRandom(self) -> int:
        # Your implementation here
        return random.choice(self.elements)