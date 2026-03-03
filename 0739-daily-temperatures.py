class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0 for _ in range(len(temperatures))]
        # [(temp, idx)]
        stack: list[int, int] = []
        for i, t in enumerate(temperatures):
            # Mark all days that today is warmer day than any day prior
            while stack and t > stack[-1][0]:
                _, popped_idx = stack.pop()
                res[popped_idx] = i - popped_idx
            stack.append((t, i))
        
        return res