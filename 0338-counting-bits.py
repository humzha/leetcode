class Solution:
    def countBits(self, n: int) -> list[int]:
        """
        Given an integer n, return an array ans of length n + 1 such
        that for each i (0 <= i <= n), ans[i] is the number of 1's
        in the binary representation of i.

        Args:
            n (int): The upper bound integer.

        Returns:
            List[int]: A list where the i-th element is the count
            of 1's in the binary representation of i.

        9 = 8 + 1
        10 = 8 + 2
        All numbers are just the biggest 2**x that fit in it, and then add the other number thats the difference of
        dp[i] = dp[biggest_2_base_fit_expo] + dp[difference]
        """
        res = [0 if i == 0 else None for i in range(n + 1)]
        i = 1
        while i < len(res):
            res[i] = 1
            i *= 2

        max_power_two = 2
        for i in range(3, n + 1):
            if res[i] is None:
                res[i] = res[i - max_power_two] + 1
            else:
                max_power_two = i
        return res
