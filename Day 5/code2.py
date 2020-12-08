def main():
    with open('input', 'r') as file:
        lines = file.read().splitlines()
        binLines = [line.replace('F', '0').replace('B', '1').replace('R', '1').replace('L', '0') for line in lines]
        seatIDs = [int(binLine, 2) for binLine in binLines]
        seatIDs.sort()
        allSeats = range(8, seatIDs[-1] - 8)
        openSeats = set(allSeats) - set(seatIDs)
        print(openSeats)
        return openSeats[0]


if __name__ == "__main__":
    print(main())
