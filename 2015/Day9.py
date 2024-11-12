
def part1():
    # I *think* everything is connected to everything here
    # so we don't really have to do node traversal fun stuff
    # but also, maybe in part 2
    distLut = {}

    with open('day9.txt', 'r') as file:
        for line in file:
            (places, dist) = [a.strip() for a in line.split(" = ")]
            (p1, p2) = [p.strip() for p in places.split(" to ")]
            dist = int(dist)

            if p1 not in distLut:
                distLut[p1] = { p2: dist}
            else:
                distLut[p1][p2] = dist

            if p2 not in distLut:
                distLut[p2] = { p1: dist}
            else:
                distLut[p2][p1] =  dist

            shortestDist = 999999
            shortestChain = []

        for place in distLut:
            # Shortest routes are going to mirror start/end 
            # if we would be the current shortest end
            # just skip it
            if len(shortestChain) >= 1 and place == shortestChain[-1]:
                continue

            routeDist, chain = findShortestRoute(distLut, place, [])
            if routeDist < shortestDist:
                shortestDist = routeDist
                shortestChain = chain
            
        print (shortestDist)
        print (shortestChain)
        
def findShortestRoute(distLut, start, currentChain: list):
    currentChain.append(start)

    chainLen = 0
    if len(distLut) == len(currentChain):
        last = None
        for entry in currentChain:
            if last is not None:
                chainLen += distLut[last][entry]
            last = entry
        
        return chainLen, currentChain

    shortestFound = 9999999
    shortestChain = []
    
    for place in distLut[start]:
        if place not in currentChain:
            dist, chain = findShortestRoute(distLut, place, currentChain.copy())
            if dist < shortestFound:
                shortestChain = chain
                shortestFound = dist
    
    return shortestFound, shortestChain

def findLongestRoute(distLut, start, currentChain: list):
    currentChain.append(start)

    chainLen = 0
    if len(distLut) == len(currentChain):
        last = None
        for entry in currentChain:
            if last is not None:
                chainLen += distLut[last][entry]
            last = entry
        
        return chainLen, currentChain

    longestFound = 0
    longestChain = []
    
    for place in distLut[start]:
        if place not in currentChain:
            dist, chain = findLongestRoute(distLut, place, currentChain.copy())
            if dist > longestFound:
                longestChain = chain
                longestFound = dist
    
    return longestFound, longestChain

def part2():
    distLut = {}

    with open('day9.txt', 'r') as file:
        for line in file:
            (places, dist) = [a.strip() for a in line.split(" = ")]
            (p1, p2) = [p.strip() for p in places.split(" to ")]
            dist = int(dist)

            if p1 not in distLut:
                distLut[p1] = { p2: dist}
            else:
                distLut[p1][p2] = dist

            if p2 not in distLut:
                distLut[p2] = { p1: dist}
            else:
                distLut[p2][p1] =  dist

            longestDist = 0
            longestChain = []

        for place in distLut:
            # Routes are still mirrored... so skip any w/ our same start/end
            if len(longestChain) >= 1 and place == longestChain[-1]:
                continue

            routeDist, chain = findLongestRoute(distLut, place, [])
            if routeDist > longestDist:
                longestDist = routeDist
                longestChain = chain
            
        print (longestDist)
        print (longestChain)
        

part1()
part2()