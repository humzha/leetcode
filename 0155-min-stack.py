from typing import Optional, List


class MinStack:
    """A stack that supports push, pop, top, and retrieving the minimum element in constant time."""

    def __init__(self) -> None:
        """Initialize your data structure here."""
        self.stack: List[int] = []
        self.min_stack: List[int] = []

    def push(self, val: int) -> None:
        """Pushes an element val onto the stack.

        Args:
            val (int): The value to push onto the stack.
        """
        if self.getMin() is None:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.getMin()))
        self.stack.append(val)

    def pop(self) -> None:
        """Removes the element on the top of the stack."""
        self.min_stack.pop()
        return self.stack.pop()

    def top(self) -> Optional[int]:
        """Gets the top element of the stack.

        Returns:
            Optional[int]: The top element if the stack is not empty, else None.
        """
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self) -> Optional[int]:
        """Retrieves the minimum element in the stack.

        Returns:
            Optional[int]: The minimum element if the stack is not empty, else None.
        """
        if not self.min_stack:
            return None
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.get_min()
