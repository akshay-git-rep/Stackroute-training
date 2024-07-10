marks = int(input("Enter the marks:"))

if marks >= 75:
    print("Distention")
elif marks >= 60:
    print("First")
elif marks >= 45:
    print("Second")
elif marks >= 33:
    print("Third")
elif marks <= 32:
    print("Fail")
else:
    print("please enter the valid marks")
    