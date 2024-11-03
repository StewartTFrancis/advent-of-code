
def part1():
    totPaper = 0

    with open('day2.txt', 'r') as file:
        for line in file:
            (l, w, h) =  [int(s) for s in line.split('x')]
            s1 = l * w
            s2 = l * h
            s3 = w * h

            size = (2 * (s1 + s2 + s3)) + min(s1, s2, s3)
            totPaper += size
    
    print (totPaper)
        

def part2():
    totRibbon = 0

    with open('day2.txt', 'r') as file:
        for line in file:
            sizes =  [int(s) for s in line.split('x')]
            sizes.sort()

            size = ((sizes[0] + sizes[1]) * 2) + (sizes[0] * sizes[1] * sizes[2])
            totRibbon += size
    
    print (totRibbon)
        

part1()
part2()