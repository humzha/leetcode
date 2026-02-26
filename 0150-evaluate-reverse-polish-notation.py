from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Evaluate the value of an arithmetic expression in Reverse
        Polish Notation.

        The valid operators are +, -, *, and /. Each operand may
        be an integer or another expression in Reverse Polish
        Notation. Division between two integers should truncate
        toward zero.

        Args:
            tokens (List[str]): The list of tokens in RPN.

        Returns:
            int: The result of evaluating the RPN expression.
        """
        c_to_op = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y),
        }
        stack = []
        for t in tokens:
            # -11.isnumeric() -> False
            if t.isnumeric() or t[1:].isnumeric():
                stack.append(int(t))
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(c_to_op[t](a, b))
        return stack.pop()
