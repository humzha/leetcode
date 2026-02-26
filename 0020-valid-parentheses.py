class Solution:
    def isValid(self, s: str) -> bool:
        # Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
        # Stack of left parens to be terminated
        stack = []
        right_to_left = {")": "(", "}": "{", "]": "["}
        left = "([{"
        for c in s:
            if c in left:
                stack.append(c)
            else:
                if not stack or stack.pop() != right_to_left[c]:
                    return False
        return not stack
