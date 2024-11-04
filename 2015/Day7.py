def part1():
    circ = {}

    with open('day7.txt', 'r') as file:
        for line in file:
            (action, target) = [e.strip() for e in line.split(" -> ")]

            circ[target] = action
        
        # Given we are *only* concerned w/ output on a
        # We can start w/ a and work backwards

        print (CalcCirc(circ, "a"))

# Since there are expensive chains getting called over and over
# Use a look up table to avoid recalculating the same wire values
wireLut = {}
def CalcCirc(circ: tuple[str, str], wire: str):
    # valid actions are:
    # an int, ex: 123
    # a wire, ex: x
    # x AND y
    # x OR y
    # x LSHIFT 2
    # x RSHIFT 2
    # NOT x

    if wire.isdigit():
        return int(wire)

    if wire in wireLut:
        return wireLut[wire]

    action = circ[wire]

    if action.isdigit():
        wireLut[wire] = int(circ[wire])
        return wireLut[wire]
    elif "AND" in action:
        (w1, w2) = action.split(" AND ")
        wireLut[wire] = (CalcCirc(circ, w1) & CalcCirc(circ, w2)) & 0xffff
        return wireLut[wire]
    elif "OR" in action:
        (w1, w2) = action.split(" OR ")
        wireLut[wire] = (CalcCirc(circ, w1) | CalcCirc(circ, w2)) & 0xffff
        return wireLut[wire]
    elif "LSHIFT" in action:
        (w1, amt) = action.split(" LSHIFT ")
        wireLut[wire] = (CalcCirc(circ, w1) << int(amt)) & 0xffff
        return wireLut[wire]
    elif "RSHIFT" in action:
        (w1, amt) = action.split(" RSHIFT ")
        wireLut[wire] = (CalcCirc(circ, w1) >> int(amt)) & 0xffff
        return wireLut[wire]
    elif "NOT" in action:
        w1 = action[4:]
        wireLut[wire] = ~CalcCirc(circ, w1) & 0xffff
        return wireLut[wire]
    else: # assume it's just a wire to wire.
        wireLut[wire] = CalcCirc(circ, action) & 0xffff
        return wireLut[wire]

def part2():
    circ = {}

    with open('day7.txt', 'r') as file:
        for line in file:
            (action, target) = [e.strip() for e in line.split(" -> ")]

            circ[target] = action
        
        a = CalcCirc(circ, "a")
        # Now, take the signal you got on wire a, 
        # override wire b to that signal, 
        # and reset the other wires (including wire a). 
        # What new signal is ultimately provided to wire a?
        wireLut.clear()

        circ['b'] = f"{a}"

        print (CalcCirc(circ, "a"))

part1()
part2()