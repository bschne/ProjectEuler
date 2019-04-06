#!/usr/bin/env python3


letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def solve(input_list):
    names = input_list[0][1:-1].split('","')
    names.sort()
    accum = 0
    for idx, name in enumerate(names):
        mult = idx + 1
        ltrsum = 0
        for c in name:
            ltrsum += letters.find(c) + 1

        score = mult * ltrsum
        accum += score

    return accum


if __name__ == "__main__":
    with open("./Problem0022.input") as f:
        input_list = f.readlines()

    print(solve(input_list))
