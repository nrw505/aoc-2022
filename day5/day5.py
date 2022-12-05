#!/usr/bin/env python
from collections import deque

def split_into_chunks(input, chunk_size):
    return [input[i:i+chunk_size] for i in range(0, len(input), chunk_size)]

def read_stacks(input):
    line = input.readline().strip()
    stacks = []
    while line != '':
        boxes = split_into_chunks(line, 4)
        for index, box in enumerate(boxes):
            if index >= len(stacks):
                stacks.extend([deque()])
            if box[0] == '[':
                stacks[index].appendleft(box[1])
        line = input.readline().strip()
    return stacks

def execute_instructions_part1(stacks, input):
    line = input.readline().strip()
    while line:
        (_, count, _, source, _, dest) = line.split(' ')
        count = int(count)
        source = int(source) - 1
        dest = int(dest) - 1
        for i in range(0, count):
            x = stacks[source].pop()
            stacks[dest].append(x)
        line = input.readline().strip()

def execute_instructions_part2(stacks, input):
    line = input.readline().strip()
    while line:
        (_, count, _, source, _, dest) = line.split(' ')
        count = int(count)
        source = int(source) - 1
        dest = int(dest) - 1
        tmp = deque()
        for i in range(0, count):
            tmp.appendleft(stacks[source].pop())
        for i in range(0, count):
            stacks[dest].append(tmp.popleft())
        line = input.readline().strip()
        
def part1():
    input = open("input.txt", "r")
    stacks = read_stacks(input)
    execute_instructions_part1(stacks, input)

    output = ''
    for stack in stacks:
        output += stack[len(stack)-1]

    print(f"message: {output}")


def part2():
    input = open("input.txt", "r")
    stacks = read_stacks(input)
    execute_instructions_part2(stacks, input)

    output = ''
    for stack in stacks:
        output += stack[len(stack)-1]

    print(f"message: {output}")

part1()
part2()
