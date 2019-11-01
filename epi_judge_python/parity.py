from test_framework import generic_test

def parity(x):
    result = 0

    while(x > 0):
        result ^= 1
        x = x & (x -1)

    return result


# def num_bits(x):
#     bits = 0

#     while(x > 0):
#         bits += x & 1
#         x = x >> 1

#     return bits

# if __name__ == '__main__':
#     exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
