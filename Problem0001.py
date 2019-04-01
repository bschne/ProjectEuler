#!/usr/bin/env python3
from math import floor


def solve(upper_bound):
    accum = 0
    for i in range(upper_bound):
        if i % 3 == 0 or i % 5 == 0:
            accum += i

    return accum


if __name__ == "__main__":
    upper_bound = 1000
    print(solve(upper_bound))
