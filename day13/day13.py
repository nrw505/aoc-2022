#!/usr/bin/env python

from sys import argv
from functools import reduce, cmp_to_key
from operator import iconcat

def compare(a, b):
    #print(f"compare {a} vs {b}")
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return -1
        elif a == b:
            return 0
        else:
            return 1
    elif isinstance(a, int) and isinstance(b, list):
        return compare([a], b)
    elif isinstance(a, list) and isinstance(b, int):
        return compare(a, [b])
    else:
        # both are lists
        i = 0
        while i < len(a) and i < len(b):
            tmp = compare(a[i], b[i])
            if tmp == -1:
                return -1
            elif tmp == 1:
                return 1
            i += 1
        if len(a) < len(b):
            return -1
        elif len(a) == len(b):
            return 0
        else:
            return 1
        

input = open(argv[1], 'r')

pairs = input.read().split("\n\n")

def part1(pairs):
    indices = []
    for i, pair in enumerate(pairs):
        (a, b) = pair.strip().split("\n")
        a = eval(a)
        b = eval(b)
        res = compare(a, b)
        if res  == -1:
            indices.append(i+1)

    print(f"part 1: {sum(indices)}")

def part2(pairs):
    all_packets = [
        [[2]],
        [[6]],
    ]
    for pair in pairs:
        (a, b) = pair.strip().split("\n")
        all_packets.append(eval(a))
        all_packets.append(eval(b))

    sorted_packets = sorted(all_packets, key=cmp_to_key(compare))
    index1 = sorted_packets.index([[2]]) + 1
    index2 = sorted_packets.index([[6]]) + 1
    decoder_key = index1 * index2
    print(f"part 2: {decoder_key}")


part1(pairs)
part2(pairs)
