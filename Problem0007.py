#!/usr/bin/env python3
from math import sqrt, floor


def is_prime(number):
    upper_bound = floor(sqrt(number))

    for i in range(2, upper_bound + 1):
        if number % i == 0:
            return False

    return True


def solve(input_no):
    primes = []
    lower_bound = 2
    while len(primes) < input_no:
        if is_prime(lower_bound):
            primes.append(lower_bound)

        lower_bound += 1

    return primes[input_no - 1]


if __name__ == "__main__":
    input_no = 10001
    print(solve(input_no))
