import os
import re
ruleParse = re.compile(r'(?P<name>[\w ]+): (?P<min1>\d+)-(?P<max1>\d+) or (?P<min2>\d+)-(?P<max2>\d+)')


def main():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input'), 'r') as file:
        lines = file.read().split('\n\n')
        rules = lines[0].splitlines()
        myTicket = lines[1].splitlines()[1]
        myTicket = [int(val) for val in myTicket.split(',')]
        tickets = lines[2].splitlines()[1:]
        tickets = [[int(val) for val in ticket.split(',')] for ticket in tickets]
        allValid = set()
        validTickets = []
        ruleDict = {}
        final = 1
        for rule in rules:
            valid = set()
            match = ruleParse.match(rule)
            min1 = int(match.group('min1'))
            max1 = int(match.group('max1'))
            for i in range(min1, max1 + 1):
                valid.add(i)
            min2 = int(match.group('min2'))
            max2 = int(match.group('max2'))
            for i in range(min2, max2 + 1):
                valid.add(i)
            name = match.group('name')
            ruleDict[name] = valid
            allValid |= valid
        for ticket in tickets:
            invalid = False
            for value in ticket:
                if value not in allValid:
                    invalid = True
                    break
            if not invalid:
                validTickets.append(ticket)

        possibles = []
        for idx in range(len(validTickets[0])):
            poss = []
            for key in ruleDict.keys():
                passing = True
                for ticket in validTickets:
                    val = ticket[idx]
                    if val not in ruleDict[key]:
                        passing = False
                        break
                if passing:
                    poss.append(key)
            possibles.append(poss)
        keys = [key for key in ruleDict.keys()]
        while keys:
            for kidx, key in enumerate(keys):
                count = 0
                loc = 0
                for idx, poss in enumerate(possibles):
                    if key in poss:
                        count += 1
                        loc = idx
                    if count > 1:
                        break
                if count < 2:
                    keys.pop(kidx)
                    possibles[loc] = key
        print(possibles)
        for idx, field in enumerate(possibles):
            if field.startswith('departure'):
                final *= myTicket[idx]
        return final


if __name__ == "__main__":
    print(main())
