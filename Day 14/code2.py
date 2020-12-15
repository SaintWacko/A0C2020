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
                addrs = ['']
                match = reMem.match(line)
                loc = match.group('loc')
                val = match.group('val')
                loc = list(f'{int(loc):036b}')
                for idx in range(len(loc)):
                    addrs2 = []
                    if mask[idx] == '0':
                        for idx2, addr in enumerate(addrs):
                            addrs2.append(addr + loc[idx])
                    elif mask[idx] == '1':
                        for idx2, addr in enumerate(addrs):
                            addrs2.append(addr + '1')
                    else:
                        for idx2, addr in enumerate(addrs):
                            addrs2.append(addr + '1')
                            addrs2.append(addr + '0')
                    addrs = addrs2
                for addr in addrs:
                    mem[addr] = int(val)

        return sum(mem.values())


if __name__ == "__main__":
    print(main())
