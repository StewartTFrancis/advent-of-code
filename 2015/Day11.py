input = "hepxcrrq"

def part1():
    currPwd = incrementPwd(input)
    
    while not isValid(currPwd):
        currPwd = incrementPwd(currPwd)

    print(currPwd)
    return currPwd

def incrementPwd(password):
    pwdList = list(password)
    idx = len(pwdList) - 1

    while True:
        if (pwdList[idx] == 'z'):
            pwdList[idx] = 'a'
            idx -= 1
        else:
            pwdList[idx] = chr(ord(pwdList[idx]) + 1)
            return "".join(pwdList)

def isValid(password):
    foundDouble = 0
    foundDoubleAt = 0

    charCodeCount = 0

    if 'i' in password or 'o' in password or 'l' in password:
        return False

    for idx, char in enumerate(password):
        if idx > 0 and char == password[idx -1] and idx > foundDoubleAt + 1:
            foundDouble += 1
            foundDoubleAt = idx

        if charCodeCount < 2:
            if idx > 0 and ord(char) == (ord(password[idx -1]) + 1):
                charCodeCount += 1
            else:
                charCodeCount = 0

    return foundDouble >= 2 and charCodeCount >= 2


def part2():
    currPwd = incrementPwd('hepxxyzz')
    
    while not isValid(currPwd):
        currPwd = incrementPwd(currPwd)

    print(currPwd)
    return currPwd

part1()
part2()