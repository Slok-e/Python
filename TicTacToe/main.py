# Base for the Game board

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

# Use list comprehension to change the input into a list
# This could be tic tac toe
choice = [int(x) for x in position]

if choice[0] == 1 and choice[1] == 1:
    map[0][0] = "X"
if choice[0] == 2 and choice[1] == 1:
    map[0][1] = "X"
if choice[0] == 3 and choice[1] == 1:
    map[0][2] = "X"
if choice[0] == 1 and choice[1] == 2:
    map[1][0] = "X"
if choice[0] == 1 and choice[1] == 3:
    map[2][0] = "X"
if choice[0] == 2 and choice[1] == 2:
    map[1][1] = "X"
if choice[0] == 2 and choice[1] == 3:
    map[2][1] = "X"
if choice[0] == 3 and choice[1] == 2:
    map[1][2] = "X"
if choice[0] == 3 and choice[1] == 3:
    map[2][2] = "X"

# Reprint Board with iinput
print(f"{row1}\n{row2}\n{row3}")
