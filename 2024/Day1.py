
def part1():
    with open('2024/day1.txt', 'r') as file:
        l1, l2 = [], []

        diff = 0
        for line in file:
            a, b = [int(s) for s in line.split("   ")]
            l1.append(int(a))
            l2.append(int(b))

        l1.sort()
        l2.sort()

        for i in range(len(l1)):
            diff += abs(l1[i] - l2[i])
        
        print(diff)

def part2():
    with open('2024/day1.txt', 'r') as file:
        l1, l2 = [], {}

        diff = 0
        for line in file:
            a, b = [int(s) for s in line.split("   ")]
            l1.append(int(a))
            if b in l2:
                l2[b] += 1
            else:
                l2[b] = 1

        l1.sort()

        for i in l1:
            if i in l2:
                diff += i * l2[i]
        
        print(diff)
        

part1()
part2()