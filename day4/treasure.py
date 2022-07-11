
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print("Enterr the coordinates: ")
column = int(input("Enter the column: "))
row = int(input("Enter the row: "))
map[column][row] = "X"
print(f"{row1}\n{row2}\n{row3}")