def is_eligible_to_vote():
    age_difference=0
    age=int(input("enter your age:"))
    if age==18:
        print("Welcome to voting:")
    elif age > 18:
        age_difference=age-18
       
        print(f"your age is {age_difference} years more than 18,You are eligible to vote")
        return True
    elif age < 18:
        age_difference=18-age
       
        print(f"your age is {age_difference} years less than 18,You are  not eligible to vote")
        return False
    else:
        print("you have entered a wrong age")  

is_eligible_to_vote()