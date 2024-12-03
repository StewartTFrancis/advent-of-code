import re

def part1():
    with open('2024/day3.txt', 'r') as file:
        tot = 0
        
        for line in file:
            muls = re.findall('mul\\(\\d+,\\d+\\)', line)

            for mul in muls:
                a, b = [int(s) for s in mul[4:-1].split(',')]
                tot += a * b

        print (tot)
                

def part2():
    with open('2024/day3.txt', 'r') as file:
        tot = 0
        active = True

        for line in file:
            commands = re.findall('mul\\(\\d+,\\d+\\)|do\\(\\)|don\'t\\(\\)', line)

            for command in commands:
                match command:
                    case 'don\'t()':
                        active = False
                    case 'do()':
                        active = True
                    case _:
                        a, b = [int(s) for s in command[4:-1].split(',')]
                        if active : tot += a * b

        print (tot)

part1()
part2()