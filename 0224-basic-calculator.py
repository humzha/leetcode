class Solution:
    """Solution for evaluating a basic arithmetic expression with parentheses.

    Given a string s representing a valid expression with '+', '-', '(',
    ')', and spaces, evaluate it and return the result. Do not use eval().
    '-' can be used as a unary operator.
    """

    def calculate(self, s: str) -> int:
        # Accumulated expression value of the current 1-deep 2-deep nested () we're on
        res: int = 0
        # Accumulated number when building 123486
        curr: int = 0
        # Last sign seen determines the value of the next expression -(3+4) or accumulated number - 3
        sign: int = 1
        stack: list[int] = []

        for c in s:
            if c.isnumeric():
                curr = curr * 10 + int(c)
            elif c in '+-':
                res += curr * sign
                sign = 1 if c == '+' else -1
                curr = 0
            elif c == '(':
                # Open a i + 1 deeper nested ()
                stack.append(res)
                stack.append(sign)
                # Set the stage to evaluate the i + 1 deeper nested (expr)
                res = 0
                sign = 1
            elif c == ')':
                # Finish evaluating the current i + 1, return to i
                res += curr * sign
                res *= stack.pop()
                res += stack.pop()
                curr = 0
                # Don't need to set sign, another sign is guaranteed if the expression has more tokens
        return res + curr * sign