my_bag = 'shiny gold'


def main():
    bags = [my_bag]
    with open('input', 'r') as file:
        lines = file.read().splitlines()
        idx = 0
        while idx < len(bags):
            bag = bags[idx]
            for line in lines:
                if bag in line:
                    nextBag = ' '.join(line.split(' ')[:2])
                    if nextBag not in bags:
                        bags.append(nextBag)
            idx += 1
    return len(bags) - 1


if __name__ == "__main__":
    print(main())
