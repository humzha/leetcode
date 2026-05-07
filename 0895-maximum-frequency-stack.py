from collections import defaultdict

class FreqStack:
    """Stack that pops the most frequent element.

    Design a stack-like data structure where pop() returns the most
    frequent element in the stack. If there is a tie, the element that
    was pushed most recently among them is popped.
    """

    def __init__(self):
        # Your implementation here
        self.max_freq: int = 0
        self.freq_to_stack = defaultdict(list)
        self.val_to_freq = defaultdict(int)
        pass

    def push(self, val: int) -> None:
        self.val_to_freq[val] += 1
        self.freq_to_stack[self.val_to_freq[val]].append(val)
        
        if self.val_to_freq[val] > self.max_freq:
            self.max_freq = self.val_to_freq[val]

    def pop(self) -> int:
        # Guaranteed non empty
        res = self.freq_to_stack[self.max_freq].pop()
        # if we don't have any more members that are of max_freq
        # Go down to the next lower frequency
        if not self.freq_to_stack[self.max_freq]:
            self.max_freq -= 1
        self.val_to_freq[res] -= 1
        return res