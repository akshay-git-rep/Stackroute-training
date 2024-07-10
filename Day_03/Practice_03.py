row_value = int(input("Enter the vlaue of row:"))

for row in range(1, row_value + 1):
    print(" " * (row_value - row), end="")
    for right_column in range(1, row + 1):
        print(right_column, end="")
    for left_column in range(row - 1, 0, -1):
        print(left_column, end="")
    print()