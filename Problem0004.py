#!/usr/bin/env python3


def corresponding_index(index, length):
    return length - index - 1


def is_palindrome(number):
    numstr = str(number)
    numstr_len = len(numstr)
    for idx, char in enumerate(numstr):
        if numstr[corresponding_index(idx, numstr_len)] != char:
            return False

    return True


def solve(lower_bound, upper_bound):
    i = upper_bound
    palindromes = []
    while i >= lower_bound:
        j = upper_bound
        while j >= lower_bound:
            if is_palindrome(i * j):
                palindromes.append(i * j)

            j -= 1

        i -= 1

    palindromes.sort(reverse=True)
    return palindromes[0]


if __name__ == "__main__":
    lower_bound = 100
    upper_bound = 999
    print(solve(lower_bound, upper_bound))
