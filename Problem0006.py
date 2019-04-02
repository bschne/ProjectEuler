#!/usr/bin/env python3


def sum_of_first_n(n):
    return n * (n + 1) / 2


def sum_of_squares_of_first_n(n):
    accum = 0
    for i in range(1, n + 1):
        accum += i ** 2

    return accum


def solve(n):
    return sum_of_first_n(n) ** 2 - sum_of_squares_of_first_n(n)


if __name__ == "__main__":
    input_no = 100
    print(solve(input_no))
