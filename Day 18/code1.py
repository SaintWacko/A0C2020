import os


def main():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input'), 'r') as file:
        lines = file.read().splitlines()
        total = 0
        for line in lines:
            total += doMath(list(line.replace(' ', '')))
        return total


def doMath(line):
    stat = []
    while line:
        if line[0] == '(':
            line.pop(0)
            stat.append(doMath(line))
        elif line[0] == ')':
            line.pop(0)
            break
        elif line[0].isnumeric():
            stat.append(int(line.pop(0)))
        else:
            stat.append(line.pop(0))
    val = stat.pop(0)
    statIt = iter(stat)
    for op in statIt:
        if op == '*':
            val *= next(statIt)
        else:
            val += next(statIt)
    return val

        



if __name__ == "__main__":
    print(main())
