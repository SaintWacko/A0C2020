import os


def main():
    acc = 0
    next = 0
    accStore = 0
    nextStore = 0
    sim = False
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input'), 'r') as file:
        lines = file.read().splitlines()
        lineStore = lines[:]  # make a backup of the program
        while True:
            instruction = lines[next].split(' ')
            if instruction[0] == 'acc':  # accumulator command
                acc += int(instruction[1])
                lines[next] = ''  # clear out this command so we can tell if we're looping
                next += 1

            elif instruction[0] == 'jmp':  # jump command
                if not sim:  # if we're not currently simulating a jmp/nop swap
                    accStore = acc
                    nextStore = next + int(instruction[1])  # store the results of the jump command
                    lines[next] = ''
                    next += 1  # then proceed as though it were a noop command
                    sim = True  # mark that we're now in a simulation
                else:  # if we're already simulating a jmp/nop swap
                    lines[next] = ''
                    next += int(instruction[1])  # proceed as normal

            else:  # noop command
                if not sim:
                    accStore = acc
                    nextStore = next + 1
                    lines[next] = ''
                    next += int(instruction[1])
                    sim = True
                else:
                    lines[next] = ''
                    next += 1
            if next == len(lines):  # if we've got the program terminating properly
                return acc
            if not lines[next]:  # if the next command is empty, we're looping
                sim = False  # exit the simulation
                lines = lineStore[:]  # restore the program from the backup
                acc = accStore  # restore the accumulator value from before the simulation
                next = nextStore  # restore the next instruction pointer from before the simulation


if __name__ == "__main__":
    print(main())
