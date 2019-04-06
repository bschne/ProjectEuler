#!/usr/bin/env python3


def read_input(input_filename):
    data = []
    with open(input_filename) as f:
        for l in f:
            li = l.replace("\n", "")
            line = []
            for n in li.split(" "):
                line.append(int(n))

            data.append(line)

    return data


def solve(input_data):
    i = len(input_data) - 2
    while i > -1:
        for idx, num in enumerate(input_data[i]):
            a = input_data[i + 1][idx]
            b = input_data[i + 1][idx + 1]
            if a > b:
                input_data[i][idx] += input_data[i + 1][idx]
            else:
                input_data[i][idx] += input_data[i + 1][idx + 1]

        i -= 1

    return input_data[0][0]


if __name__ == "__main__":
    input_data = read_input("./Problem0018.input")
    print(solve(input_data))
