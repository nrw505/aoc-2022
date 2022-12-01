#!/usr/bin/env python

lines = open("input.txt", "r").readlines()

def part1(lines):
    meals = [[]]
    totals = [0]
    current_elf = 0

    for line in lines:
        line = line.strip()
        if len(line) == 0:
            current_elf += 1
            meals.append([])
            totals.append(0)
        else:
            calories = int(line)
            meals[current_elf].append(calories)
            totals[current_elf] += calories

    print(f"Max calories is {max(totals)}\n")

def part2(lines):
    meals = [[]]
    totals = [0]
    current_elf = 0

    for line in lines:
        line = line.strip()
        if len(line) == 0:
            current_elf += 1
            meals.append([])
            totals.append(0)
        else:
            calories = int(line)
            meals[current_elf].append(calories)
            totals[current_elf] += calories

    top_three = list(reversed(sorted(totals)))[0:3]
    print(f"Total top 3 calories is {sum(top_three)}\n")

part1(lines)
part2(lines)
