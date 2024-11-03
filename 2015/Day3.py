# Since an infinite grid is probably a bit much for memory constraints
# We're going to cheat and use a set that keeps track of a string representing
# x/y coordinates of places where presents are dropped.
def part1():
    x, y = 0, 0

    presents = set()

    stringFormat = "{0},{1}"

    with open('day3.txt', 'r') as file:
        for line in file:
            for char in line:
                match char: 
                    case '^':
                        y += 1
                    case 'v':
                        y -= 1
                    case '<':
                        x -= 1
                    case '>':
                        x += 1
                    case _:
                        print (f"uhh, what am I seeing? ""{char}""")
                presents.add(stringFormat.format(x, y))
        print (len(presents))

# I'm sorry, this is kind of ugly... but moving the logic into a single class is cleaner than trying to track multiple x/y/etcs
class SantaMover():
    x, y = 0, 0
    def move(self, char):
        match char: 
                    case '^':
                        self.y += 1
                    case 'v':
                        self.y -= 1
                    case '<':
                        self.x -= 1
                    case '>':
                        self.x += 1
                    case _:
                        print (f"uhh, what am I seeing? ""{self.char}""")
        return self.x, self.y

def part2():
    presents = set()

    stringFormat = "{0},{1}"

    santa = SantaMover()
    robosanta = SantaMover()

    with open('day3.txt', 'r') as file:
        for line in file:
            for idx, char in enumerate(line):
                if idx % 2 == 0:
                    presents.add(stringFormat.format(*santa.move(char))) # Sorry again. A single tuple is returned, this unpacks it
                else:
                    presents.add(stringFormat.format(*robosanta.move(char)))
                
        print (len(presents))

part1()
part2()