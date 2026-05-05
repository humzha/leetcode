class Solution:
    """Solution for sorting an array without built-in functions.

    Given an array of integers nums, sort it in ascending order
    in O(nlog(n)) time with the smallest space complexity possible.
    """

    def sortArray(self, nums: list[int]) -> list[int]:
        def merge(a: list[int], b: list[int]) -> int:
            res = []
            a_idx = b_idx = 0
            while a_idx < len(a) or b_idx < len(b):
                a_val = a[a_idx] if a_idx < len(a) else float('inf')
                b_val = b[b_idx] if b_idx < len(b) else float('inf')
                if a_val < b_val:
                    res.append(a_val)
                    a_idx += 1
                else:
                    res.append(b_val)
                    b_idx += 1
            return res

            
        # Your implementation here
        def merge_sort(nums: list[int]) -> list[int]: 
            """
            Sort s[l: r + 1]
            """
            if not nums or len(nums) <= 1:
                return nums
            l, r = 0, len(nums) - 1
            m = (l + r) // 2

            a = merge_sort(nums[0: m + 1])
            b = merge_sort(nums[m + 1:])
            
            return merge(a, b)

        return merge_sort(nums)