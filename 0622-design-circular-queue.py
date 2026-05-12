class MyCircularQueue:
    """Circular queue (ring buffer) implementation.

    Design a circular queue that follows FIFO principle where the last
    position connects back to the first position. Supports enQueue, deQueue,
    Front, Rear, isEmpty, and isFull operations.
    """

    def __init__(self, k: int):
        # Your implementation here
        self.capacity = k
        self.data = [None for _ in range(k)]
        # Inclusive
        self.head = self.tail = 0
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        # If it's empty, don't increment when it's inclusive
        if not self.isEmpty():
            self.tail = (self.tail + 1) % self.capacity

        # Increment by 1
        self.data[self.tail] = value

        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        # If the size is 1, don't advance the head pointer
        if self.size > 1:
            self.head = (self.head + 1) % self.capacity

        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.tail]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity