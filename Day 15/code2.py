import os


def main():
    lastIdx = {}
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input'), 'r') as file:
        input = file.read()
        line = input.split(',')
        for idx, val in enumerate(line[:-1]):
            lastIdx[int(val)] = idx
        lastVal = int(line[-1])
        nextVal = 0
        for idx in range(len(line) - 1, 30000000 - 1):
            if lastVal in lastIdx:
                nextVal = idx - lastIdx[lastVal]
            else:
                nextVal = 0
            lastIdx[lastVal] = idx
            lastVal = nextVal
        return lastVal


if __name__ == "__main__":
    print(main())
