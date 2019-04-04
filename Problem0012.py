#!/usr/bin/env python3
from math import floor


def divisors(num):
    divs = []
    upper_bound = num
    i = 1
    while i < upper_bound:
        if num % i == 0:
            divs.append(i)
            divs.append(num / i)
            upper_bound = num / i

        i += 1

    return divs


def solve(min_divisors):
    curr_trinum = 1
    i = 2
    while True:
        if len(divisors(curr_trinum)) > min_divisors:
            break

        curr_trinum += i
        i += 1

    return curr_trinum


if __name__ == "__main__":
    print(solve(500))
    # input_no = 500
    # print(solve(input_no))
