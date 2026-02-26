from typing import List


class Solution:
    """Solution for searching a target value in a rotated sorted array.

    You are given an integer array nums sorted in ascending order with distinct
    values, which may have been rotated at an unknown pivot. Given the array
    after rotation and an integer target, return the index of target if it is
    in nums, or -1 if it is not in nums. :contentReference[oaicite:0]{index=0}
    """

    def search(self, nums: List[int], target: int) -> int:
        """Finds the index of the target in the rotated sorted array.

        Args:
            nums (List[int]): The possibly rotated array of distinct integers.
            target (int): The integer to search for.

        Returns:
            int: The index of target if found; otherwise -1.
        """
        # 0) Find the index of rotation
        # 1) Given the index of rotation, we can convert the array's index to where it would
        # be in a sorted array w/o rotation

        def find_rot_idx(nums: List[int]) -> int:
            # 4,5,6,7,0,1,2], target = 3
            #       m
            # 4,5,6,0,1,2,3], target = 3
            # 0 1 2 3 4 5 6
            # 4,0,1,2,3,4,5], target = 3
            # 0 1 2 3 4 5 6
            # l     r
            # l r
            #   lr
            l, r = 0, len(nums) - 1
            while l < r:
                print(l, r)
                m = (l + r) // 2
                if nums[m] > nums[r]:
                    l = m + 1
                else:
                    r = m
            print(l, r)
            return l

        l, r = 0, len(nums) - 1
        rot_idx = find_rot_idx(nums)

        def si_to_ri(i: int) -> int:
            # sort index -> rot index
            # [4,5,6,7,0,1,2]
            # [0,1,2,4,5,6,7]
            #  0 1 2 3 4 5 6
            # 3 -> 0
            # 3
            return (i + rot_idx) % len(nums)

        while l <= r:
            m = (l + r) // 2
            if nums[si_to_ri(m)] == target:
                return si_to_ri(m)
            elif target > nums[si_to_ri(m)]:
                l = m + 1
            else:
                r = m - 1
        return -1
