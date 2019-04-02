#!/usr/bin/env python3
from math import sqrt, floor


def is_prime(number):
    upper_bound = floor(sqrt(number))

    for i in range(2, upper_bound + 1):
        if number % i == 0:
            return False

    return True


def solve(input_no):
    i = floor(sqrt(input_no))
    while i > 1:
        i -= 1
        if input_no % i == 0 and is_prime(i):
            return i


if __name__ == "__main__":
    input_no = 600851475143
    # input_no = 13195
    print(solve(input_no))
