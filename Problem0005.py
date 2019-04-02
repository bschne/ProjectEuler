#!/usr/bin/env python3


def satisfies_constraint(upper_bound, number):
    i = 2
    while i <= upper_bound:
        if number % i != 0:
            return False

        i += 1

    return True


def solve(upper_bound):
    i = 0
    while True:
        i += 1
        if satisfies_constraint(upper_bound, i):
            return i


if __name__ == "__main__":
    upper_bound = 20
    print(solve(upper_bound))
