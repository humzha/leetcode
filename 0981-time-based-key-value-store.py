import collections
from typing import Dict, Tuple, Callable


def bisect_right(nums: List[int], t: int, key: Callable[[Any], Any]) -> int:
    lo, hi = 0, len(nums)
    while lo < hi:
        m = (lo + hi) // 2
        if key(nums[m]) <= t:
            lo = m + 1
        else:
            hi = m
    return lo


class TimeMap:
    def __init__(self):
        self.key_to_tv: Dict[str, Tuple[int, str]] = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Calls to set are strictly increasing
        self.key_to_tv[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_to_tv:
            return ""
        i = bisect_right(self.key_to_tv[key], timestamp, key=lambda x: x[0])
        if i == 0:
            return ""
        return self.key_to_tv[key][i - 1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
