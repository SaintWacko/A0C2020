import os
import re


def main():
    mem = {}
    mask = ''
    reMask = re.compile(r'mask = (?P<mask>[01X]+)')
    reMem = re.compile(r'mem\[(?P<loc>\d+)\] = (?P<val>\d+)')
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input'), 'r') as file:
        lines = file.read().splitlines()
        for line in lines:
            if line[:2] == 'ma':
                match = reMask.match(line)
                mask = list(match.group('mask'))
            else:
                match = reMem.match(line)
                loc = match.group('loc')
                val = match.group('val')
                val = list(f'{int(val):036b}')
                for idx in range(len(val)):
                    if mask[idx] != 'X':
                        val[idx] = mask[idx]
                mem[loc] = int(''.join(val), 2)
        return sum(mem.values())


if __name__ == "__main__":
    print(main())
