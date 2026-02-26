from test_framework import generic_test


def parity(x: int) -> int:
    # Parity is whether the # of bits in a number is odd
    res = 0
    while x:
        # Clears the lowest set bit in x
        x = x & (x - 1)
        res ^= 1
    return res


if __name__ == "__main__":
    exit(generic_test.generic_test_main("parity.py", "parity.tsv", parity))
