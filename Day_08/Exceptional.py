while True:
    try:
        a = int(input("Enter the value of first number :"))
        b = int(input("Enter the value of second number :"))
        div = a / b

    except ZeroDivisionError:
        print("zero division error")

    except ValueError:
        print("invalid value")
        continue
    else:
        print(f"{div:.3f}")
        break
    finally:
        print("finally executed") 