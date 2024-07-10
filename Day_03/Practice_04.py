value = int(input("Enter the vlaue of row:"))

for row in range(value):
    for column in range(value):
        if row == column or row + column == (value - 1):
            print("1", end="")
        else:
            print("0", end="")
    print()