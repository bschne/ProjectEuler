#!/usr/bin/env python3
from math import sqrt


def eratosthenes(upper_bound):
    primes = [True for i in range(upper_bound + 1)]
    primes[0] = False
    primes[1] = False
    primes[2] = True

    i = 2
    while i <= sqrt(upper_bound):
        if primes[i]:
            j = 0
            while i ** 2 + j * i <= upper_bound:
                primes[i ** 2 + j * i] = False
                j += 1

        i += 1

    ret = []
    for idx, val in enumerate(primes):
        if val:
            ret.append(idx)

    return ret


def solve(input_no):
    primes = eratosthenes(input_no)
    accum = 0
    for i in primes:
        accum += i

    return accum


if __name__ == "__main__":
    input_no = 2000000
    print(solve(input_no))
