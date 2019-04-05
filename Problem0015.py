#!/usr/bin/env python3
from math import factorial


def solve(grid_length):
    return int(factorial(2 * grid_length) / (factorial(grid_length) ** 2))


if __name__ == "__main__":
    grid_length = 20
    print(solve(grid_length))
