#!/usr/bin/env python

def part1(string):
    for i in range(4, len(string)):
        chars = set(string[i-4:i])
        if len(chars) == 4:
            print(f"4 unique after {i} characters")
            return
    print("no unique sets of 4")

def part2(string):
    for i in range(14, len(string)):
        chars = set(string[i-14:i])
        if len(chars) == 14:
            print(f"14 unique after {i} characters")
            return
    print("no unique sets of 14")

string = open("input.txt", "r").readline()

part1('bvwbjplbgvbhsrlpgdmjqwftvncz')
part1('nppdvjthqldpwncqszvftbrmjlhg')
part1(string)

part2('mjqjpqmgbljsphdztnvjfqwrcgsmlb')
part2('bvwbjplbgvbhsrlpgdmjqwftvncz')
part2('nppdvjthqldpwncqszvftbrmjlhg')
part2(string)
