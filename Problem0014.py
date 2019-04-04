#!/usr/bin/env python3


def solve(upper_bound):
    starting_number = 1
    chain_cache = {}
    while True:
        chain = []
        current_no = starting_number
        while True:
            chain.append(current_no)

            if current_no == 1:
                break

            if current_no % 2 == 0:
                current_no /= 2
            else:
                current_no = current_no * 3 + 1

            if current_no < starting_number:
                chain.extend(chain_cache[current_no])
                break

        chain_cache[starting_number] = chain
        starting_number += 1
        if starting_number > upper_bound:
            break

    maxlen = 0
    maxlen_starting_no = 0
    for k in chain_cache.keys():
        if len(chain_cache[k]) > maxlen:
            maxlen = len(chain_cache[k])
            maxlen_starting_no = k

    return maxlen_starting_no


if __name__ == "__main__":
    print(solve(1000000))
