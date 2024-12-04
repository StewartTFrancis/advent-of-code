import re

def part1():
    with open('2024/day3.txt', 'r') as file:
        tot = 0
        
        # Pretty spot on use-case for regex.
        for line in file:
            muls = re.findall('mul\\(\\d+,\\d+\\)', line)

            for mul in muls:
                # We *could* use capture groups to avoid having to do string splicing here
                # But it's simple/fast enough
                a, b = [int(s) for s in mul[4:-1].split(',')]
                tot += a * b

        print (tot)
                

def part2():
    with open('2024/day3.txt', 'r') as file:
        tot = 0
        active = True

        for line in file:
            # Find all the things we care about.
            commands = re.findall('mul\\(\\d+,\\d+\\)|do\\(\\)|don\'t\\(\\)', line)

            # At least we don't need to build a whole state machine in here.
            # Just run through in order and update the active flag as we see
            # do's and don'ts
            for command in commands:
                match command:
                    case 'don\'t()':
                        active = False
                    case 'do()':
                        active = True
                    case _:
                        if active:
                            a, b = [int(s) for s in command[4:-1].split(',')]
                            tot += a * b

        print (tot)

part1()
part2()