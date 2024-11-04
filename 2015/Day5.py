def part1():

    vowels = ['a','e','i','o','u']
    disallowed = ['ab', 'cd', 'pq', 'xy']

    niceWords = 0

    with open('day5.txt', 'r') as file:
        for word in file:
            vowelCount = 0
            foundDouble = False
            foundDWord = False

            for idx, char in enumerate(word):
                if idx > 0 and char == word[idx -1]:
                    foundDouble = True

                if char in vowels:
                    vowelCount += 1
            
            if vowelCount >= 3 and foundDouble:
                for dword in disallowed:
                    if dword in word:
                        foundDWord = True
                        break
                
                if not foundDWord:
                    niceWords += 1

        print (niceWords)

def part2():
    niceWords = 0
   
    with open('day5.txt', 'r') as file:
        for word in file:
            foundTwoTwice = False
            foundRepeat = False

            wordLen = len(word)
            for idx, char in enumerate(word):
                jump = idx + 2

                if jump >= wordLen:
                    break

                if word[jump] == char:
                    foundRepeat = True
                
                for idy, char in enumerate(word[jump:]):
                    if word[idx:idx + 2] == word[idy + jump:2 + idy + jump]:
                        foundTwoTwice = True

            
            if foundTwoTwice and foundRepeat:
                niceWords += 1
        
        print (niceWords)

part1()
part2()