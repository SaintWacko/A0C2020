import os

MY_BAG = 'shiny gold'

lineDict = {}


def main():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input'), 'r') as file:
        lines = file.read().splitlines()
        for line in lines:
            key = ' '.join(line.split(' ')[:2])
            value = []
            lineArray = line.split(' ')
            for idx, word in enumerate(lineArray):
                if word.isdigit():
                    value.append((word, ' '.join(lineArray[idx + 1:idx + 3])))
            lineDict[key] = value
    return get_contents(MY_BAG)


def get_contents(bag):
    bag_data = lineDict[bag]
    if not bag_data:
        return 0
    count = 0
    for data in bag_data:
        bagsInside = get_contents(data[1])
        bags = int(data[0]) + int(data[0]) * bagsInside
        count += bags
    return count


if __name__ == "__main__":
    print(main())
