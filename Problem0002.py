#!/usr/bin/env python3


def solve(upper_bound):
    accum = 0
    prev = 1
    curr = 2

    while curr < upper_bound:
        if curr % 2 == 0:
            accum += curr

        tmp = curr
        curr = prev + curr
        prev = tmp

    return accum


if __name__ == "__main__":
    upper_bound = 4000000
    print(solve(upper_bound))
