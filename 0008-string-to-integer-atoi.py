class Solution:
    """Solution for converting a string to a 32-bit signed integer (atoi).

    Implement `myAtoi(string)`, which converts a string to a 32-bit signed integer
    (similar to C/C++’s `atoi`). The function first discards as many whitespace
    characters as necessary until the first non-whitespace character is found.
    Then, starting from this character, takes an optional initial plus or minus
    sign followed by as many numerical digits as possible, and interprets them as
    a numerical value. The string can contain additional characters after those
    that form the integral number, which are ignored and have no effect on the
    behavior of this function. If the first sequence of non-whitespace characters
    is not a valid integral number, no conversion is performed. The function
    returns the valid 32-bit signed integer representation of this number. The
    environment is assumed to store 32-bit integers, so values outside the
    signed 32-bit range [−2³¹, 2³¹ − 1] should be clamped.
    """

    def myAtoi(self, s: str) -> int:
        """Converts the input string to a 32-bit signed integer, clamped to the
        range [−2³¹, 2³¹ − 1].

        Args:
            s (str): The string to convert.

        Returns:
            int: The converted integer.
        """
        s = s.strip()
        if not s:
            return 0
        negative = s[0] == "-"
        if s[0] in "+-":
            s = s[1:]
        elif not s[0].isnumeric():
            return 0

        res = 0
        for c in s:
            if not c.isnumeric():
                break
            res *= 10
            res += ord(c) - ord("0")

        if negative:
            res *= -1

        if res < -(2**31):
            res = -(2**31)
        if res > (2**31) - 1:
            res = (2**31) - 1

        return res
