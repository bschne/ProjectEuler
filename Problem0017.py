#!/usr/bin/env python3
from math import floor


base_words = {0: "",
              1: "one",
              2: "two",
              3: "three",
              4: "four",
              5: "five",
              6: "six",
              7: "seven",
              8: "eight",
              9: "nine",
              10: "ten",
              11: "eleven",
              12: "twelve",
              13: "thirteen",
              14: "fourteen",
              15: "fifteen",
              16: "sixteen",
              17: "seventeen",
              18: "eighteen",
              19: "nineteen",
              20: "twenty",
              30: "thirty",
              40: "forty",
              50: "fifty",
              60: "sixty",
              70: "seventy",
              80: "eighty",
              90: "ninety",
              100: "hundred",
              1000: "thousand"}


def to_words(number):
    if number > 999:
        thousands = floor(number / 1000)
        remainder = number - thousands * 1000
        return base_words[thousands] + base_words[1000] + to_words(remainder)

    if number > 99:
        hundreds = floor(number / 100)
        remainder = number - hundreds * 100
        andword = ("", "and")[remainder > 0]
        return base_words[hundreds] + base_words[100] + \
            andword + to_words(remainder)

    if number > 19:
        tens = floor(number / 10) * 10
        remainder = number - tens
        return base_words[tens] + to_words(remainder)

    return base_words[number]


def solve(upper_bound):
    accum = 0
    for n in range(1, upper_bound + 1):
        accum += len(to_words(n))

    return accum


if __name__ == "__main__":
    upper_bound = 1000
    print(solve(upper_bound))
