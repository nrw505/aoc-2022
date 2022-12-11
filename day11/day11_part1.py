#!/usr/bin/env python

import re
from collections import deque
from math import floor
from sys import argv

MONKEY_RE = re.compile("""Monkey ([0-9]*):
  Starting items: (.*)
  Operation: new = (.*)
  Test: divisible by ([0-9]*)
    If true: throw to monkey ([0-9]*)
    If false: throw to monkey ([0-9]*)"""
)

def parse_monkeys(input):
    data = input.read()
    return [
        {
            'number': int(match[0]),
            'items': deque([int(item) for item in match[1].split(', ')]),
            'operation': match[2],
            'divisor': int(match[3]),
            'true': int(match[4]),
            'false': int(match[5]),
        }
        for match in MONKEY_RE.findall(data)
    ]

def run_monkey(monkeys, i, inspections):
    monkey = monkeys[i]
    while monkey['items']:
        inspections[i] += 1
        old = monkey['items'].popleft()
        new = eval(monkey['operation'], {}, {'old': old})
        new = floor(new / 3)
        remainder = new % monkey['divisor']
        destination = monkey['false']
        if remainder == 0:
            destination = monkey['true']
        monkeys[destination]['items'].append(new)

def run_monkeys(monkeys, inspections):
    for i in range(0, len(monkeys)):
        run_monkey(monkeys, i, inspections)
    
monkeys = parse_monkeys(open(argv[1], 'r'))
inspections = [0] * len(monkeys)

for i in range(0, 20):
    run_monkeys(monkeys, inspections)


inspections.sort()
inspections.reverse()
(a, b) = inspections[0:2]

monkey_business = a * b

print(f"monkey business: {monkey_business}")
