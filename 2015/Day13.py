
import os
from itertools import permutations

os.chdir("./2015")

def part1():
    with open('day13.txt', 'r') as file:
        happiness = {}

        # Build the happiness dictionary from our input
        for line in file:
            chunks = line.split(" ")
            name = chunks[0]
            action = chunks[2]
            value = int(chunks[3])
            if action == "lose":
                value = -value
            target = chunks[-1].strip()[:-1]

            if name not in happiness:
                happiness[name] = {}
            happiness[name][target] = value

        # Calculate the maximum happiness by trying all seating arrangements
        from itertools import permutations
        max_happiness = float('-inf')
        for arrangement in permutations(happiness.keys()):
            total = 0
            for i in range(len(arrangement)):
                left = arrangement[i - 1]
                right = arrangement[(i + 1) % len(arrangement)]
                total += happiness[arrangement[i]][left] + happiness[arrangement[i]][right]
            max_happiness = max(max_happiness, total)
        print(max_happiness)
        

def part2():
    with open('day13.txt', 'r') as file:
        happiness = {}

        # Build the happiness dictionary from our input
        for line in file:
            chunks = line.split(" ")
            name = chunks[0]
            action = chunks[2]
            value = int(chunks[3])
            if action == "lose":
                value = -value
            target = chunks[-1].strip()[:-1]

            if name not in happiness:
                happiness[name] = {}
            happiness[name][target] = value

        for name in happiness.keys():
            happiness[name]["Me"] = 0
        happiness["Me"] = {}
        for name in happiness.keys():
            happiness["Me"][name] = 0

        # Calculate the maximum happiness by trying all seating arrangements
        max_happiness = float('-inf')
        for arrangement in permutations(happiness.keys()):
            total = 0
            for i in range(len(arrangement)):
                left = arrangement[i - 1]
                right = arrangement[(i + 1) % len(arrangement)]
                total += happiness[arrangement[i]][left] + happiness[arrangement[i]][right]
            max_happiness = max(max_happiness, total)
        print(max_happiness)
        

part1()
part2()