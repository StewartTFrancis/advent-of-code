def part1():

    vowels = ['a','e','i','o','u']
    disallowed = ['ab', 'cd', 'pq', 'xy']

    niceWords = 0

    with open('day5.txt', 'r') as file:
        for word in file:
            vowelCount = 0
            foundDouble = False
            for idx, char in enumerate(word):
                if idx > 0 and char == word[idx -1]:
                    foundDouble = True

                if char in vowels:
                    vowelCount += 1
            
            if vowelCount > 3 and foundDouble:
                foundDWord = False

                for dword in disallowed:
                    if dword in word:
                        foundDWord = True
                
                if not foundDWord:
                    niceWords += 1

        print (niceWords)

            


def part2():
    with open('day5.txt', 'r') as file:
        for line in file:
            for idx, char in enumerate(line):
                print (idx)
                
        #print (len(presents))

part1()
#part2()