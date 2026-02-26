import math


class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Given an integer x, determine whether it is a palindrome.
        An integer is a palindrome when it reads the same forward
        and backward.

        Args:
            x (int): The integer to check.

        Returns:
            bool: True if x is a palindrome, False otherwise.
        """

        # 121
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        elif x < 10:
            return True
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + (x % 10)
            x //= 10

        return x == reversed_half or x == reversed_half // 10
