import functools

class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        nums = [str(x) for x in nums]
        def cmp(a: str, b: str) -> int:
            if a + b > b + a:
                return -1
            return 1
            
        nums.sort(key=functools.cmp_to_key(cmp))
        
        return str(int(''.join(nums)))