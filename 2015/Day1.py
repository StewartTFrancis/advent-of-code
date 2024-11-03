
def part1():
    currFloor = 0

    with open('day1.txt', 'r') as file:
        for line in file:
            for char in line:
                if char == '(':
                    currFloor += 1
                elif char == ')':
                    currFloor -= 1
        print(currFloor)

def part2():
    currFloor = 0

    with open('day1.txt', 'r') as file:
        for line in file:
            for idx, char in enumerate(line):
                if char == '(':
                    currFloor += 1
                elif char == ')':
                    currFloor -= 1
                if currFloor < 0:
                    print (idx + 1)
                    return
        

part1()
part2()