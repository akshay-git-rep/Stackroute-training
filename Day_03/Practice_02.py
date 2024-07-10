row_value = int(input("Enter the vlaue of row:"))

for row in range(1, row_value + 1):
    print(" " * (row_value - row), end="")
    for column in range(1, row + 1):
        print(column, end="")
    print()