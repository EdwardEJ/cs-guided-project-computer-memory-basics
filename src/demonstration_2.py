"""
Given an unsigned integer, write a function that returns the number of '1' bits
that the integer contains (the
[Hamming weight](https://en.wikipedia.org/wiki/Hamming_weight))

Unsigned: the integer can only represent positive numbers

String representation of numbers
Integer representation of numbers
Binary representation of numbers

Examples:

- `hamming_weight(n = 00000000000000000000001000000011) -> 3`
- `hamming_weight(n = 00000000000000000000000000001000) -> 1`
- `hamming_weight(n = 11111111111111111111111111111011) -> 31`

Notes:

- "Unsigned Integers (often called "uints") are just like integers (whole
numbers) but have the property that they don't have a + or - sign associated
with them. Thus they are always non-negative (zero or positive). We use uint's
when we know the value we are counting will always be non-negative."
"""
def hamming_weight(n: int) -> int:
    # Your code here
    # if we're given a `normal` unsigned integer, how do we convert it?
    # using `&`, we have a way to check the right most bit of n to see if it equals 1
    # the `>>` operator allows us to `move` the bitwise digits over one spot to the right
    # when do we stop right shifting?
    # we can stop n shifting when n == 0
    # return the number of `1`s in the bitewise representation of the number 

    # counter = 0
    # while n != 0:
    #   if n & 1 == 1:
    #     counter += 1
    #   n = n >> 1
    # return counter

    # counter = 0
    # bin_rep = bin(n)

    # for i in range(len(bin_rep)):
    #     if bin_rep[i] == '1':
    #       counter += 1
    # return counter

    return bin(n).count('1')
