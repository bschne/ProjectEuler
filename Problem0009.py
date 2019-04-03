#!/usr/bin/env python3
from math import sqrt


def is_pythagorean_triplet(a, b, c):
    return (a < b < c) and (a ** 2 + b ** 2 == c ** 2)


def solve(target_sum):
    current_sum = 0
    a = 1
    c = 0

    while True:
        b = 1
        while a + b + c < 1000:
            b += 1
            c = sqrt(a ** 2 + b ** 2)
            if c.is_integer() and is_pythagorean_triplet(a, b, c):
                break

        if a + b + c == 1000:
            break

        a += 1

    return a * b * c


if __name__ == "__main__":
    print(solve(1000))
