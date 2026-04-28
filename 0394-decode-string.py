class Solution:
    """Solution for decoding an encoded string.

    Given an encoded string `s`, return its decoded version. The encoding rule is:
    k[encoded_string], where the substring inside the brackets is repeated `k` times.

    You may assume:
    - `k` is a positive integer
    - The input string is always valid
    - No digits appear except as repeat counts
    """  

    def decodeString(self, s: str) -> str:
        """Decodes the given encoded string.

        Args:
            s (str): The encoded string.

        Returns:
            str: The fully decoded string.
            
        In the stack there are two valid types:
        - alphanumeric characters
        - [ marks the start of the string pattern
        """

        stack = []
        i = 0
        while i < len(s):
            c = s[i]
            if c.isalnum() or c == '[':
                stack.append(c)
            else:
                encoded_str = []
                while stack[-1] != '[':
                    encoded_str.append(stack.pop())

                encoded_str = ''.join(reversed(encoded_str))
                stack.pop() # ']'
                freq = []
                while stack and stack[-1].isnumeric():
                    freq.append(stack.pop())
                stack.append(int(''.join(reversed(freq))) * encoded_str)
            i += 1
        return ''.join(stack)