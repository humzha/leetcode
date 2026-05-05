class Solution:
    """Solution for finding all elements that appear more than ⌊n/3⌋ times.

    Given an integer array of size n, return all elements that appear
    more than ⌊n/3⌋ times. Follow up: solve in linear time with O(1) space.
    """

    def majorityElement(self, nums: list[int]) -> list[int]:
        # Your implementation here
        mp = {}
        for n in nums:
            if n not in mp:
                mp[n] = 1
            else:
                mp[n] += 1
            if len(mp) == 3:
                for k in mp.keys():
                    mp[k] -= 1
                    if mp[k] == 0:
                        del mp[k]

        res = []
        for candidate in mp.keys():
            if nums.count(candidate) > (len(nums) / 3):
                res.append(candidate)
        return res