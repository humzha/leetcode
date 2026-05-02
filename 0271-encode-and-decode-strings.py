class Codec:
    """Solution for encoding and decoding a list of strings.

    Design an algorithm to encode a list of strings into a single string
    and decode it back to the original list.

    Requirements:
    - Must handle any ASCII characters (including delimiters)
    - Encoding must be unambiguous
    """

    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string.

        Args:
            strs (list[str]): List of strings.

        Returns:
            str: Encoded string.
        """
        res = []
        for word in strs:
            res.append(str(len(word)))
            res.append('#')
            res.append(word)
        return ''.join(res)

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings.

        Args:
            s (str): Encoded string.

        Returns:
            list[str]: Original list of strings.
        """
        res = []
        curr_word_len = 0
        i = 0
        # 01234
        # 2#ab
        while i < len(s):
            if s[i].isnumeric():
                curr_word_len = curr_word_len * 10 + int(s[i])
                i += 1
            # Read number already
            if s[i] == '#':
                res.append(s[i + 1: i + 1 + curr_word_len])
                i += 1 + curr_word_len
        return res

codec = Codec()

arr = ['#12321', '#21abc']
assert codec.decode(codec.encode(arr)) == arr

print(codec.encode(arr))
print(codec.decode(codec.encode(arr)))