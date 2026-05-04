class Solution:
    """Solution for computing trapped rainwater.

    Given n non-negative integers representing an elevation map where
    the width of each bar is 1, compute how much water it can trap after raining.
    """

    def trap(self, height: list[int]) -> int:
        # Your implementation here
        max_l = []
        curr_max = 0
        for h in height:
            max_l.append(curr_max)
            curr_max = max(h, curr_max)
            
        curr_max = 0
        max_r = []
        for i in range(len(height) - 1, -1 ,-1):
            max_r.append(curr_max)
            curr_max = max(height[i], curr_max)
        max_r.reverse()
            
        res = 0
        for i, h in enumerate(height):
            area = min(max_l[i], max_r[i]) - h
            if area > 0:
                res += area
        return res