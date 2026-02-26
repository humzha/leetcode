class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        addend_to_idx = {}
        for i, n in enumerate(nums):
            # target = n + prev_addend
            # n = target - prev_addend
            prev_addend = target - n
            if prev_addend in addend_to_idx:
                return (addend_to_idx[prev_addend], i)
            addend_to_idx[n] = i
        return (-1, -1)
