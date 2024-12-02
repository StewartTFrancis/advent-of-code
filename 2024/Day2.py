
def part1():
    with open('2024/day2.txt', 'r') as file:
        safeCount = 0
        curr, prev = 0, 0
        ascending = True
        unsafe = False

        for line in file:
            unsafe = False
            for idx, s in enumerate(line.split(" ")):
                curr = int(s)

                if idx > 0:
                    if idx == 1:
                        ascending = curr > prev
                    elif ascending and curr < prev:
                        unsafe = True
                    elif not ascending and curr > prev:
                        unsafe = True

                    if abs(curr - prev) < 1 or abs(curr - prev) > 3:
                        unsafe = True
                
                prev = curr
            
            if not unsafe:
                safeCount += 1

        print (safeCount)

def safeCheck(arr):
    curr, prev = 0, 0
    ascending = True
    unsafe = False
    
    for idx, s in enumerate(arr):
        
        curr = s

        if idx > 0:
            if idx == 1:
                ascending = curr > prev
            elif ascending and curr < prev:
                unsafe = True
            elif not ascending and curr > prev:
                unsafe = True

            if abs(curr - prev) < 1 or abs(curr - prev) > 3:
                unsafe = True
        
        prev = curr
        
    return not unsafe

def part2():
    with open('2024/day2.txt', 'r') as file:
        safeCount = 0

        for line in file:
            arr = [int(s) for s in line.split(" ")]
            
            if safeCheck(arr):
                safeCount += 1
            else:
                for i in range(len(arr)):
                    curr = arr.copy()
                    del curr[i]
                
                    if safeCheck(curr):
                        safeCount += 1
                        break

        print (safeCount)

part1()
part2()