import os


def main():
    acc = 0
    next = 0
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input'), 'r') as file:
        lines = file.read().splitlines()
        while lines[next]:
            instruction = lines[next].split(' ')
            if instruction[0] == 'acc':
                acc += int(instruction[1])
                lines[next] = ''
                next += 1
            elif instruction[0] == 'jmp':
                lines[next] = ''
                next += int(instruction[1])
            else:
                lines[next] = ''
                next += 1
        return acc


if __name__ == "__main__":
    print(main())
