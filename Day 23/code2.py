import os


def main():
    lines = []
    cups = []
    current = 0
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input'), 'r') as file:
        lines = file.read().splitlines()
        iCups = [int(cup) for cup in list(lines[0])]
        cups = list(range(1, 1000001))
        cups.append(iCups[0])
        cups[0] = -1
        current = iCups[0]
        for idx, cup in enumerate(iCups[:len(iCups) - 1]):
            cups[cup] = iCups[idx + 1]
        cups[iCups[-1]] = len(iCups) + 1

    def move():
        nonlocal cups
        nonlocal current
        moving = []
        moving.append(cups[current])
        moving.append(cups[moving[-1]])
        moving.append(cups[moving[-1]])
        dest = current
        while dest in moving or dest == current:
            if dest == 1:
                dest = len(cups) - 1
            else:
                dest -= 1
        cups[current], cups[dest], cups[moving[2]] = cups[moving[2]], moving[0], cups[dest]
        current = cups[current]

    def printCups():
        current = 1
        pCups = []
        # for _ in range(len(cups) - 1):
        for _ in range(100):
            pCups.append(current)
            current = cups[pCups[-1]]
        return pCups
            
    for x in range(10000000):
        move()
    a = cups[1]
    b = cups[a]
    print(a)
    print(b)
    return a * b
    


if __name__ == "__main__":
    print(main())
