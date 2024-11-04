
def part1():
    totLen = 0
    totParsedLen = 0

    with open('day8.txt', 'r') as file:
        for line in file:
            line = line.strip() # strip newline

            totLen += len(line)

            parsedLen = 0
            skipNext = 0

            for idx, char in enumerate(line):
                if skipNext > 0:
                    skipNext -= 1
                    continue

                if char == '\\':
                    if line[idx + 1] == 'x':
                        parsedLen += 1
                        skipNext = 3
                    elif line[idx + 1] == '\\':
                        parsedLen += 1
                        skipNext = 1
                    else:
                        parsedLen += 1
                        skipNext = 1
                elif char != '"':
                    parsedLen += 1

            totParsedLen += parsedLen
        
        print (f"{totLen} - {totParsedLen} = {totLen - totParsedLen}")
        print (totLen - totParsedLen)

def part2():
    totLen = 0
    totParsedLen = 0

    with open('day8.txt', 'r') as file:
        for line in file:
            line = line.strip() # strip newline

            totLen += len(line)

            parsedLen = 2

            for char in enumerate(line):
                if char == '\\':
                    parsedLen += 2
                elif char == '"':
                    parsedLen += 2
                else:
                    parsedLen += 1

            totParsedLen += parsedLen
        
        print (f"{totParsedLen} - {totLen} = {totParsedLen - totLen}")
        print (totParsedLen - totLen)
        

#part1()
part2()