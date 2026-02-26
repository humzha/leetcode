class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Given two binary strings a and b, return their sum as a
        binary string.

        Args:
            a (str): A binary string.
            b (str): Another binary string.

        Returns:
            str: The binary string representing the sum of a and b.

        """

        def _and(a: str, b: str) -> str:
            a_idx, b_idx = len(a) - 1, len(b) - 1
            res = []
            while a_idx >= 0 or b_idx >= 0:
                a_val = a[a_idx] if a_idx >= 0 else "0"
                b_val = b[b_idx] if b_idx >= 0 else "0"
                if a_val == b_val == "1":
                    res.append("1")
                else:
                    res.append("0")
                a_idx -= 1
                b_idx -= 1
            return "".join(reversed(res))

        def _xor(a: str, b: str) -> str:
            # Ensure a is the smaller one
            if len(a) > len(b):
                a, b = b, a
            a_idx, b_idx = len(a) - 1, len(b) - 1
            res = []
            while a_idx >= 0 and b_idx >= 0:
                if (a[a_idx], b[b_idx]).count("1") == 1:
                    res.append("1")
                else:
                    res.append("0")
                a_idx -= 1
                b_idx -= 1

            return b[: b_idx + 1] + "".join(reversed(res))

        def strip_leading(s: str) -> str:
            for i in range(len(s)):
                if s[i] == "1":
                    return s[i:]
            return "0"

        if b == "0":
            return a

        xor_addend = _xor(a, b)
        carry_over = _and(a, b) + "0"
        return self.addBinary(strip_leading(xor_addend), strip_leading(carry_over))
