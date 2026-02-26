from typing import List


class Solution:
    """Solution for generating letter combinations of a phone number.

    Given a string `digits` containing digits from `'2'` to `'9'`, return all
    possible letter combinations that the number could represent. The mapping
    from digits to letters is the same as on a standard phone keypad, and
    the answer can be returned in any order.
    """

    def letterCombinations(self, digits: str) -> List[str]:
        """Generates all possible letter combinations for the given digit string.

        Args:
            digits (str): A string of digits from `'2'` to `'9'`.

        Returns:
            List[str]: All possible letter combinations that the number could represent.
        """
        digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []

        def gen_combo(i: int, p: List[str]):
            if i == len(digits):
                res.append("".join(p))
                return
            for c in digit_to_letters[digits[i]]:
                p.append(c)
                gen_combo(i + 1, p)
                p.pop()

        gen_combo(0, [])
        return res
