import hashlib

def part1():
    key = "yzbqklnj"
    x = 0

    while True:
        curr = f"{key}{x}"

        result = hashlib.md5(curr.encode()).hexdigest()

        if result[:5] == '00000':
            break
        
        x += 1

    print (x)


def part2():
    key = "yzbqklnj"
    x = 0

    while True:
        curr = f"{key}{x}"

        result = hashlib.md5(curr.encode()).hexdigest()

        if result[:6] == '000000':
            break

        x += 1
    
    print (x)

part1()
part2()