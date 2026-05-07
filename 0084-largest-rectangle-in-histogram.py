class Solution:
    """Solution for finding the largest rectangle area in a histogram.

    Given an array of bar heights representing a histogram, find the area
    of the largest rectangle that can be formed within the histogram.
    """

    def largestRectangleArea(self, heights: list[int]) -> int:
        # [1, 2, 3]
        stack = []

        res = 0
        # Pop all remaining
        heights.append(0)
        # Your implementation here
        for i, h in enumerate(heights):
            left = i
            if not stack:
                stack.append((h, left))
            else:
                # stack = [3]
                # val = 2
                # s
                while stack and stack[-1][0] > h:
                    height, popped_left = stack.pop()
                    res = max(height * (i - popped_left), res)
                    left = popped_left
                
                # stack = [(3, 0)]
                # val = 4, i = 1
                if stack and stack[-1][0] == h:
                    continue
                # stack = [3]
                # val = 4
                stack.append((h, left))
        heights.pop()
        return res