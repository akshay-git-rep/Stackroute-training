age=int(input("enter the age:"))
day=str(input("enter day:"))
tkt_price=float(input("enter ticket price:"))
discount=float(0.0)

day = day.lower()
if (day in ("sunday","monday","tuesday","wednesday","thursday","friday","saturday","sunday")) and (age > 0):
    
    if age>=60 and age<=100 and day != "tuesday":
            discount=tkt_price*40/100
            print(f"Got a senior discount of price {discount} out of {tkt_price}")

    elif age>=25 and age<= 60 and day != "friday":
        discount=tkt_price*10/100
        print(f"Got a mid-age discount of price {discount} out of {tkt_price}")
    
    elif age>=10 and age<=25 and day == "wednesday":
        discount=tkt_price*15/100
        print(f"Got a student discount of price {discount} out of {tkt_price}")
        
    else:
        print(f"No discount your ticket price is {tkt_price}")
else:
    print("you have entered incorrect value")