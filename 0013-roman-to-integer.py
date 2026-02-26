class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Convert a Roman numeral to an integer. Roman numerals are
        represented by the characters I, V, X, L, C, D, and M with
        specific values and subtractive notation.

        Args:
            s (str): A Roman numeral string.

        Returns:
            int: The integer representation of the Roman numeral.
        """
        roman_values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        res = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman_values[s[i + 1]] > roman_values[s[i]]:
                res -= roman_values[s[i]]
            else:
                res += roman_values[s[i]]
        return res
