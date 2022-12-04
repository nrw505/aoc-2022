#!/usr/bin/env python

def string_range_to_set(string):
    (a, b) = string.split('-')
    return set(range(int(a), int(b)+1))

lines = open("input.txt", "r").readlines()
pairs = [list(map(lambda x: string_range_to_set(x), line.strip().split(','))) for line in lines]

def part1(pairs):
    count = 0
    for (a, b) in pairs:
        if a.issubset(b) or b.issubset(a):
            count += 1
    print(f"{count} fully contained")

def part2(pairs):
    count = 0
    for (a, b) in pairs:
        if any(a.intersection(b)):
            count += 1
    print(f"{count} overlap")
    

part1(pairs)
part2(pairs)
