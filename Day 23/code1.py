import os


# def main():
#     lines = []
#     with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input'), 'r') as file:
#         lines = file.read().splitlines()
#     cups = [int(cup) for cup in list(lines[0])]
#     size = len(cups)
#     current = 0

#     def move():
#         nonlocal cups
#         nonlocal current
#         moving = []
#         label = cups[current]
#         nextLabel = label
#         moving.append(cups.pop((current + 1) if current < len(cups) - 1 else 0))
#         moving.append(cups.pop((current + 1) if current < len(cups) - 1 else 0))
#         moving.append(cups.pop((current + 1) if current < len(cups) - 1 else 0))
#         print(cups)
#         print(moving)
#         next = None
#         while next is None:
#             if label == 0:
#                 label = size
#             else:
#                 label -= 1
#             try:
#                 next = cups.index(label)
#             except ValueError:
#                 pass
#         cups = cups[:next + 1] + moving + cups[next + 1:]
#         current = (cups.index(nextLabel) + 1) % len(cups)
#         print(current, ': ', cups)

#     for _ in range(100):
#         move()
def main():
    lines = []
    cups = []
    current = 0
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input'), 'r') as file:
        lines = file.read().splitlines()
        iCups = [int(cup) for cup in list(lines[0])]
        cups = list(range(len(iCups) + 1))
        # cups = list(range(10000001))
        cups[0] = -1
        print(len(cups))
        current = iCups[0]
        for idx, cup in enumerate(iCups[:len(iCups) - 1]):
            cups[cup] = iCups[idx + 1]
        cups[iCups[-1]] = iCups[0]
        # cups[iCups[-1]] = len(iCups) + 1
        print(cups[:100])
        print(cups[-100:])

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
                # dest == 1000000
                dest = len(cups) - 1
            else:
                dest -= 1
        cups[current], cups[dest], cups[moving[2]] = cups[moving[2]], moving[0], cups[dest]
        current = cups[current]

    def printCups():
        current = 1
        pCups = []
        for _ in range(len(cups) - 1):
            pCups.append(current)
            current = cups[pCups[-1]]
        return pCups
            
    for x in range(100):
        move()

    ret = printCups()
    return ''.join([str(cup) for cup in ret])


if __name__ == "__main__":
    print(main())
