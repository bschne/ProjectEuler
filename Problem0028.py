#!/usr/bin/env python3


def solve(side_length):
    spiral = [[0 for i in range(side_length)] for i in range(side_length)]
    num = side_length ** 2
    x = side_length - 1
    y = 0
    dx = -1
    dy = 0

    while num > 0:
        spiral[y][x] = num

        chdir = x + dx >= side_length or y + dy >= side_length or \
            x + dx < 0 or y + dy < 0 or \
            spiral[y + dy][x + dx] != 00

        if chdir:
            if x - 1 > -1 and spiral[y][x - 1] == 0:
                dx = -1
                dy = 0
            elif y + 1 < side_length and spiral[y + 1][x] == 0:
                dx = 0
                dy = 1
            elif x + 1 < side_length and spiral[y][x + 1] == 0:
                dx = 1
                dy = 0
            elif y - 1 > -1 and spiral[y - 1][x] == 0:
                dx = 0
                dy = -1

        x += dx
        y += dy
        num -= 1

    accum = -1
    for i in range(side_length):
        accum += spiral[i][i]
        accum += spiral[side_length - i - 1][i]

    return accum


if __name__ == "__main__":
    side_length = 1001
    print(solve(side_length))
