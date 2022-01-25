from pprint import pprint
filepath = "input4-test.txt"
#
with open(filepath) as f:
    file_list = f.readlines()

#file_list = ['7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1\n', '\n', '22 13 17 11  0\n',
#             ' 8  2 23  4 24\n', '21  9 14 16  7\n', ' 6 10  3 18  5\n', ' 1 12 20 15 19\n', '\n', ' 3 15  0  2 22\n',
#             ' 9 18 13 17  5\n', '19  8  7 25 23\n', '20 11 10 24  4\n', '14 21 16 12  6\n', '\n', '14 21 17 24  4\n',
#             '10 16 15  9 19\n', '18  8 23 26 20\n', '22 11 13  6  5\n', ' 2  0 12  3  7']

# get first line to separate out random numbers:
# called_numbers = file_list[0]
called_numbers = (list(map(int, file_list[0].strip().split(','))))  # returns a list with elements as integers

# print(called_numbers)

# split whole file by paragraph (each list element is now a paragraph:
with open(filepath) as input:
    paragraphs = input.read().split("\n\n")

f = 1  # start from 1 here not 0 as we will slice to skip first line of input and go straight to board 1.
for i in paragraphs[1:]:  # [1:] bit 'slices' and tells to start at 1 not 0 so skips first iteration
    print("board", f, "\n", i)
    f += 1

# PUT ALL BOARDS INTO A 3D NESTED ARRAY so all board data is in a single data structure.:

allboards = []

for n, paragraph in enumerate(paragraphs[1: None]):  # enumerate returns both value itself and also position not.
    twod_board = []

    for line in paragraph.split("\n"):
        # Next, .strip removes any unwanted whitespace from teh start and end of the line.  split separates the elements
        # by whitespace within the line.
        twod_board.append(list(map(int, line.strip().split())))
    # or this way would do the same:
    # twod_board.append([ int(i) for i in line.strip().split()])

    # Now Do something with twod_board (and 'n' if you like) - append to a new list/variable for later use:
    allboards.append(twod_board)

print("\nallboards:\n", allboards)

print("\n called_numbers:\n", called_numbers, "\n")

# Initial setup of an array holding binary numbers to 'flag' matches when found:

all_positions = []
board_positions = []

# Calculate lengths of various required things:
allboards_length = len(allboards)
rowcount = len(paragraph.split("\n"))
row_length = len(paragraph.split("\n")[0].split())
print("allboards_length variable is:", allboards_length)
print("rowcount variable is:", rowcount)
print("row_length variable is:", row_length)

for q in range(rowcount):
    board_positions.append([0] * row_length)

print("board_positions:\n", board_positions, "\n")

for p in range(allboards_length):
    all_positions.append(board_positions)

print("all_positions:", all_positions)

# ITERATE THROUGH ALL DATA AND PERFORM CHECKS - 4 NESTED LOOPS REQUIRED
# 1 to iterate numbers_called, the other 3 to iterate through the 3 levels of 'allboards'


for called_number in called_numbers[0: None]:

    for a, board in enumerate(allboards[0: None]):

        for b, row in enumerate(board[0: None]):

            for c, element in enumerate(row[0: None]):

                if element == called_number:
                    print("Match found at:", a, b, c, "for called number:", called_number)
                    all_positions[a][b][c] = 1
                    print("all_positions NEW: \n")
                    pprint(all_positions)


                    #At this point do a check on the current row if there are any full rows/columns:

                    if len(set(row[0:None])) == 1:
                        print("\n board:", a, "row:", b, "has a full row")
                        exit()



# CHECK:
# other_example = [[[0, 1], [2, 3]], [[4, 5], [6, 7]]]
# print(other_example, "other example BEFORE")
# other_example[0][1][0] = 8
# print(other_example, "other example AFTER")

