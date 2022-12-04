#!/usr/bin/env python

lines = open("input.txt", "r").readlines()

ME_SCORE_P1 = {
    'X': 1, # i throw rock
    'Y': 2, # i throw paper
    'Z': 3, # i throw scissors
}

OUTCOME_SCORE_P1 = {
    'X': {
        'A': 3,
        'B': 0,
        'C': 6,
    },
    'Y': {
        'A': 6,
        'B': 3,
        'C': 0,
    },
    'Z': {
        'A': 0,
        'B': 6,
        'C': 3,
    },
}

OUTCOME_SCORE_P2 = {
    'X': { # lose: 0 + value of losing throw
        'A': 3, # i throw scissors
        'B': 1, # i throw rock
        'C': 2, # i throw paper
    },
    'Y': { # draw: 3 + value of drawing throw
        'A': 4, # i throw rock
        'B': 5, # i throw paper
        'C': 6, # i throw scissors
    },
    'Z': { # win: 6 + value of winning throw
        'A': 8, # i throw paper
        'B': 9, # i throw scissors
        'C': 7, # i throw rock
    },
}

def part1(lines):
    total = 0
    for line in lines:
        line = line.strip()
        (opponent, me) = line.split(' ')
        score = ME_SCORE_P1[me] + OUTCOME_SCORE_P1[me][opponent]
        total += score
    print(f"Total score: {total}")

def part2(lines):
    total = 0
    for line in lines:
        line = line.strip()
        (opponent, outcome) = line.split(' ')
        score = OUTCOME_SCORE_P2[outcome][opponent]
        total += score
    print(f"Total score: {total}")
    
part1(lines)
part2(lines)
