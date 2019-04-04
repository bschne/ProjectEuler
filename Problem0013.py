#!/usr/bin/env python3


def read_input_nums(input_file):
    nums = []
    with open(input_file) as f:
        for line in f:
            nums.append(int(line))

    return nums


def solve(nums, no_of_digits):
    tmpsum = 0
    for i in nums:
        tmpsum += i

    return str(tmpsum)[:no_of_digits]


if __name__ == "__main__":
    input_file = "./Problem0013.input"
    no_of_digits = 10
    nums = read_input_nums(input_file)

    print(solve(nums, no_of_digits))
