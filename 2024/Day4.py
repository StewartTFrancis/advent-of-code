def isXmas(grid, y, x):
    found = 0
    
    # We could probably skip the bounds checking and just have the step directions
    # and handle the out of bounds w/ the try/except
    # But... here we are.
    backward = x > 2
    up = y > 2
    forward = x < (len(grid[y]) - 3)
    down = y < (len(grid) - 3)

    # Four cardinal directions
    if backward and isXmasCheck(grid, y, x, 0, -1):
        found += 1
    if forward and isXmasCheck(grid, y, x, 0, 1):
        found += 1
    if up and isXmasCheck(grid, y, x, -1, 0):
        found += 1
    if down and isXmasCheck(grid, y, x, 1, 0):
        found += 1
    
    # Diagonal backward
    if backward and up and isXmasCheck(grid, y, x, -1, -1):
        found += 1
    if backward and down and isXmasCheck(grid, y, x, 1, -1):
        found += 1
    
    # Diagonal forward
    if forward and up and isXmasCheck(grid, y, x, -1, 1):
        found += 1
    if forward and down and isXmasCheck(grid, y, x, 1, 1):
        found += 1

    return found
    

def isXmasCheck(grid, y, x, yStep, xStep):
    # We don't really need the try/except here since we're checking before calling
    # Just felt weird not to have it
    try:
        # Just check that it's XMAS from starting point -> direction
        return grid[y][x] == 'X' and grid[y + yStep][x + xStep] == 'M' and grid[y + (yStep * 2)][x + (xStep * 2)] == 'A' and grid[y + (yStep * 3)][x + (xStep * 3)] == 'S'
    except:
        print (f"exception at y: {y}; x: {x}; yStep {yStep}; xStep {xStep}")

def part1():
    grid = []
    found = 0

    with open('2024/day4.txt', 'r') as file:
        for line in file:
            grid.append(line)
        
        for idy, line in enumerate(grid):
            for idx, char in enumerate(line):
                if char == 'X':
                    found += isXmas(grid, idy, idx)
    
    print (found)

def isMasX(grid, y, x):
    if y == 0 or y == len(grid) -1 or x == 0 or x == len(grid[y]):
        return False
    
    # This is ugly... but basically if one corner is M the other needs to be S and vice versa
    # So, check the top-left and bottom-right, then bottom-left and top-right to make sure
    if grid[y][x] == 'A' and (
            (grid[y - 1][x - 1] == 'M' and grid[y + 1][x + 1] == 'S') or (grid[y - 1][x - 1] == 'S' and grid[y + 1][x + 1] == 'M')
        ) and (
            (grid[y + 1][x - 1] == 'M' and grid[y - 1][x + 1] == 'S') or (grid[y + 1][x - 1] == 'S' and grid[y - 1][x + 1] == 'M')
        ):
        return True

def part2():
    grid = []
    found = 0

    with open('2024/day4.txt', 'r') as file:
        for line in file:
            grid.append(line)
        
        for idy, line in enumerate(grid):
            for idx, char in enumerate(line):
                # Since we really want to check a pattern based on the center A
                if char == 'A' and isMasX(grid, idy, idx):
                    found += 1
    
    print (found)
        

part1()
part2()