#!/usr/bin/env python
lines = open("input.txt", "r").readlines()

def priority(item):
    prio = ord(item) - ord('A') + 1
    if prio <= 26:
        return prio + 26
    prio = ord(item) - ord('a') + 1
    return prio

def part1(lines):
    total = 0
    for line in lines:
        l = len(line)
        h = int(l/2)
        a = set(line[0:h])
        b = set(line[h:l])
        item = list(a.intersection(b))[0]
        total += priority(item)
    print(f"total priority: {total}")


def part2(lines):
    total = 0
    i = 0
    while i < len(lines):
        a = set(lines[i].strip())
        i += 1
        b = set(lines[i].strip())
        i += 1
        c = set(lines[i].strip())
        i += 1
        item = list(a.intersection(b).intersection(c))[0]
        total += priority(item)
    print(f"total priority: {total}")
    

part1(lines)
part2(lines)
