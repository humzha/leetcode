class Solution:
    """Solution for evaluating a basic arithmetic expression string.

    Given a string s representing an expression with '+', '-', '*', '/'
    and non-negative integers, evaluate it with correct operator precedence.
    Integer division truncates toward zero. Do not use eval().
    """

    def calculate(self, s: str) -> int:
        prev_op = '+'
        curr_num = 0
        stack = []
        for c in s + '+':
            if c.isnumeric():
                curr_num = curr_num * 10 + int(c)
            # Operator
            elif c in '+/*-':
                if prev_op == '-':
                    stack.append(curr_num * -1)
                else:
                    stack.append(curr_num)
                if prev_op == '*':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a * b)
                elif prev_op == '/':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(int(a / b))
                    
                prev_op = c
                curr_num = 0
        
        return sum(stack)