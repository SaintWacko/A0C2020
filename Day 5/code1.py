def main():
    with open('input', 'r') as file:
        lines = file.read().splitlines()
        binLines = [line.replace('F', '0').replace('B', '1').replace('R', '1').replace('L', '0') for line in lines]
        seatIDs = [int(binLine, 2) for binLine in binLines]
        seatIDs.sort()
        return seatIDs[-1]


# def main():
#     with open('input', 'r') as file:
#         lines = file.read().splitlines()
#         topSeat = ''
#         rCount = 0
#         cCount = 0
#         for line in lines:
#             r = line.count('B')
#             c = line.count('L')
#             if r > rCount:
#                 rCount = r
#                 cCount = c
#                 topSeat = line
#             elif r == rCount:
#                 if c > cCount:
#                     cCount = c
#                     topSeat = line
#         return SeatParser(topSeat).parse()

# class SeatParser():
#     def __init__(self, seat):
#         print(seat)
#         self.rows = range(128)
#         self.columns = range(8)
#         self.seatRow = list(seat[:7])
#         self.seatColumn = list(seat[7:])

#     def parse(self):
#         return self.parseRow() * 8 + self.parseColumn()

#     def parseRow(self):
#         print(self.seatRow)
#         if self.seatRow:
#             row = self.seatRow.pop()
#             print(self.seatRow)
#             if row == 'F':
#                 self.rows = self.rows[:int(len(self.rows) / 2)]
#             elif row == 'B':
#                 self.rows = self.rows[int(len(self.rows) / 2):]
#             return self.parseRow()
#         return self.rows[0]

#     def parseColumn(self):
#         print(self.seatColumn)
#         if self.seatColumn:
#             row = self.seatColumn.pop()
#             if row == 'F':
#                 self.columns = self.columns[:int(len(self.columns) / 2)]
#             elif row == 'B':
#                 self.columns = self.columns[int(len(self.columns) / 2):]
#             return self.parseColumn()
#         return self.columns[0]


if __name__ == "__main__":
    print(main())
