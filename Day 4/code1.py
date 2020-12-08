REQUIRED_KEYS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}


def main():
    with open('input', 'r') as file:
        lines = file.read().split('\n\n')
        valid = 0
        for line in lines:
            parsedLine = line.replace('\n', ' ')
            keys = [pair.split(':')[0] for pair in parsedLine.split(' ')]
            missingKeys = REQUIRED_KEYS - set(keys)
            if not len(missingKeys):
                valid += 1
    return valid


if __name__ == "__main__":
    print(main())
