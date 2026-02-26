from typing import List


class MyQueue:
    def __init__(self):
        # LIFO
        self.inbound: List[int] = []
        # FIFO
        self.outbound: List[int] = []

    def push(self, x: int) -> None:
        self.inbound.append(x)

    def pop(self) -> int:
        if self.empty():
            return -1
        self._fill_outbound()
        return self.outbound.pop()

    def _fill_outbound(self) -> None:
        # Fills outbound stack if necessary, only when it is empty
        if not self.outbound:
            while self.inbound:
                self.outbound.append(self.inbound.pop())

    def peek(self) -> int:
        if self.empty():
            return -1
        self._fill_outbound()
        return self.outbound[-1]

    def empty(self) -> bool:
        return not self.inbound and not self.outbound


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
