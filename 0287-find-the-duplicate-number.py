class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # nums[0], all vlaues are in [1..n]
        slow = fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow