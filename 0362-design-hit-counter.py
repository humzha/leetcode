from collections import deque

class HitCounter:
    """Solution for designing a hit counter.

    Design a system that counts the number of hits received in the past
    5 minutes (i.e., the past 300 seconds).

    Implement the HitCounter class:
    - HitCounter() initializes the object.
    - void hit(int timestamp) records a hit at the given timestamp.
    - int getHits(int timestamp) returns the number of hits in the past
      300 seconds from the given timestamp.

    Notes:
    - Timestamps are in seconds.
    - Calls are made in chronological (non-decreasing) order.
    - Multiple hits can occur at the same timestamp.
    """

    def __init__(self):
        """Initializes the hit counter."""
        self.q = deque()
        self.WINDOW = 300
        
    def _remove_stale_hits(self, timestamp: int):
        while self.q and self.q[0][0] < timestamp - (self.WINDOW - 1):
            self.q.popleft()

    def hit(self, timestamp: int) -> None:
        """Records a hit at the given timestamp.

        Args:
            timestamp (int): Current timestamp in seconds.
        """
        self._remove_stale_hits(timestamp)
        if self.q and self.q[-1][0] == timestamp:
            self.q[-1][1] += 1
        else:
            self.q.append([timestamp, 1])
        

    def getHits(self, timestamp: int) -> int:
        """Returns the number of hits in the past 300 seconds.

        Args:
            timestamp (int): Current timestamp in seconds.

        Returns:
            int: Number of hits within the last 5 minutes.
        """
        self._remove_stale_hits(timestamp)
        return sum(x[1] for x in self.q)
    
hc = HitCounter()
hc.hit(2)
hc.hit(2)
hc.hit(3)
assert hc.getHits(3) == 3
hc.hit(299)
assert hc.getHits(299) == 4
hc.hit(302)
assert hc.getHits(302) == 3