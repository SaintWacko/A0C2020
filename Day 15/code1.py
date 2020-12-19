import os


def main():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input'), 'r') as file:
        input = file.read()
        line = input.split(',')
        for idx in range(len(line), 2020):
            idx -= 1
            if line[idx] in line[:idx]:
                line.append(str(idx - (len(line) - 2 - line[:idx][::-1].index(line[idx]))))
            else:
                line.append('0')
    return line[-1]


if __name__ == "__main__":
    print(main())
