
def part1():
    with open('2024/day1.txt', 'r') as file:
        l1, l2 = [], []

        diff = 0
        for line in file:
            # Break up the two numbers from the input file
            a, b = [int(s) for s in line.split("   ")]

            # Add them to lists
            l1.append(a)
            l2.append(b)

        # Sort
        l1.sort()
        l2.sort()

        # Compare them and capture the delta
        for i in range(len(l1)):
            diff += abs(l1[i] - l2[i])
        
        # Print the total difference
        print(diff)

def part2():
    with open('2024/day1.txt', 'r') as file:
        # List two will be a look up this time.
        l1, l2 = [], {}

        count = 0
        for line in file:
            # Still the same parsing 
            a, b = [int(s) for s in line.split("   ")]
            # l1 will will the list we work through
            # We *could* make them both dictionaries w/ counts and then just multiply
            # Which would be an absolutely valid optimization if we were ever running this again
            l1.append(a)
            # l2 is a dict w/ total count of the times that number occurs
            if b in l2:
                l2[b] += 1
            else:
                l2[b] = 1

        # Walk through l1, adding the total to our count
        for i in l1:
            if i in l2:
                count += i * l2[i]
        
        print(count)
        

part1()
part2()