class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        Given two strings s and t, return True if they are equal
        when both are typed into empty text editors. '#' means
        a backspace character.

        Args:
            s (str): The first input string containing letters and '#'.
            t (str): The second input string containing letters and '#'.

        Returns:
            bool: True if the processed strings are equal, False otherwise.
        """

        def compute(s: str) -> str:
            stack = []
            for c in s:
                if c == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(c)
            return "".join(stack)

        return compute(s) == compute(t)
