inputVal = "1113122113"

def part1():
    currVal = inputVal
    for _ in range(40):
        currVal = makeLookSay(currVal)

    print (len(currVal))

        
def makeLookSay(input):
    retVal = ""

    currChar = ""
    currCount = 0

    for char in input:
        if currChar == char:
            currCount += 1
        else:           
            if currChar != "":
                retVal += f"{currCount}{currChar}"
            
            currChar = char
            currCount = 1
    
    retVal += f"{currCount}{currChar}"
    
    return retVal

def part2():
    currVal = inputVal
    for _ in range(50):
        currVal = makeLookSay(currVal)

    print (len(currVal))
        
part1()
part2()