from test_framework import generic_test


def swap_bits(x, i, j):
    # TODO - you fill in here.
    # A 64-bit integer can be viewed as an array of 64 bits
    # with the LSB occupying the 0th index
    # and the MSB occupying the 63rd index
    if i == j or (x >> i) & 1 == (x >> j) & 1:
        return x
    bit_mask = (1 << i) | (1 << j)
    return x ^ bit_mask


if __name__ == "__main__":
    exit(generic_test.generic_test_main("swap_bits.py", "swap_bits.tsv", swap_bits))
