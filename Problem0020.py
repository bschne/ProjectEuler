#!/usr/bin/env python3
from math import factorial


def solve(i):
    return sum(int(c) for c in str(factorial(i)))


if __name__ == "__main__":
    print(solve(100))
