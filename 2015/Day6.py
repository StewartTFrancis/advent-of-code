def part1():
    cols = 1000
    rows = 1000
    lightGrid = [[0 for i in range(cols)] for j in range(rows)]

    with open('day6.txt', 'r') as file:
        lightsOn = 0
        
        for line in file:
            # We have three basic commands:
            # turn off 660,55 through 986,197
            # turn on 158,270 through 243,802
            # toggle 223,39 through 454,511

            action = None
            coords = None

            # This is *not* defensive input checking
            # and don't ever put anything like this
            # in production. It's just fast/cheap
            if line[:4] == "turn":
                if line[5:8] == "off":
                    action = "off"
                    coords = parseCoords(line[9:])
                else:
                    action = "on"
                    coords = parseCoords(line[8:])
                
            else:
                action = "toggle"
                coords = parseCoords(line[7:])

            for x in range(coords['start'][0], coords['end'][0] + 1):
                for y in range(coords['start'][1], coords['end'][1] + 1):
                    match action: 
                        case 'off':
                            lightGrid[x][y] = False
                        case 'on':
                            lightGrid[x][y] = True
                        case 'toggle':
                            lightGrid[x][y] = not lightGrid[x][y]
            
        for row in lightGrid:
            for col in row:
                if col == True:
                    lightsOn += 1
        
        print (lightsOn)

                            

def parseCoords(textCoords):
    (startPair, endPair) = [ pair.strip() for pair in textCoords.split("through")]
    return { 
            "start": [int(xy) for xy in startPair.split(",")],
            "end":  [int(xy) for xy in endPair.split(",")],
        }

def part2():
    cols = 1000
    rows = 1000
    lightGrid = [[0 for i in range(cols)] for j in range(rows)]

    with open('day6.txt', 'r') as file:
        lightsOn = 0
        
        for line in file:
            # We have three basic commands:
            # turn off 660,55 through 986,197
            # turn on 158,270 through 243,802
            # toggle 223,39 through 454,511

            action = None
            coords = None

            # This is *not* defensive input checking
            # and don't ever put anything like this
            # in production. It's just fast/cheap
            if line[:4] == "turn":
                if line[5:8] == "off":
                    action = "off"
                    coords = parseCoords(line[9:])
                else:
                    action = "on"
                    coords = parseCoords(line[8:])
                
            else:
                action = "toggle"
                coords = parseCoords(line[7:])

            for x in range(coords['start'][0], coords['end'][0] + 1):
                for y in range(coords['start'][1], coords['end'][1] + 1):
                    match action: 
                        case 'off':
                            lightGrid[x][y] = max(lightGrid[x][y] - 1, 0)
                        case 'on':
                            lightGrid[x][y] += 1
                        case 'toggle':
                            lightGrid[x][y] += 2
            
        for row in lightGrid:
            for col in row:
                lightsOn += col
        
        print (lightsOn)
   

#part1()
part2()