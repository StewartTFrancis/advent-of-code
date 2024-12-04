
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

                # We are looking for ascending/descending... and we'll do a look back
                # So, for the first element there's nothing to look back at.
                if idx > 0:
                    # For the second element, figure out if numbers are increasing or decreasing
                    if idx == 1:
                        ascending = curr > prev
                    # For subsequent elements, make sure we're still going the same direction
                    elif ascending and curr < prev:
                        unsafe = True
                    elif not ascending and curr > prev:
                        unsafe = True

                    # Regardless of direction, make sure our change is in range
                    if abs(curr - prev) < 1 or abs(curr - prev) > 3:
                        unsafe = True
                
                prev = curr
            
            if not unsafe:
                safeCount += 1

        print (safeCount)

# For part 2, pull the safety check into a separate function
# Otherwise the 'do the check, but missing an element logic
# Gets more complicated than it should be.
def safeCheck(arr):
    curr, prev = 0, 0
    ascending = True
    unsafe = False
    
    for idx, curr in enumerate(arr):
        
        # This is all the same as day 1
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
            
            # If the line is safe no need to pull anything out
            if safeCheck(arr):
                safeCount += 1
            else:
                # If the line isn't safe, pull each element out in turn and recheck
                # until we find one that is safe or run out of elements
                # I'm sure there are less computationally exhaustive ways
                # to do this, but again, we're never running this again
                # aaaand it takes less than a second to run on my setup
                for i in range(len(arr)):
                    curr = arr.copy()
                    del curr[i]
                
                    if safeCheck(curr):
                        safeCount += 1
                        break

        print (safeCount)

part1()
part2()