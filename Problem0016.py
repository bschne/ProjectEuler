#!/usr/bin/env python3


def solve(n):
    num = 2 ** n
    tmpsum = 0
    for d in str(num):
        tmpsum += int(d)

    return tmpsum


if __name__ == "__main__":
    n = 1000
    print(solve(n))
