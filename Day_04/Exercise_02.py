import random
attempts = 5
num = random.choice(range(1,10))
 
for i in range(attempts):
    n = int(input("enter the number::"))
    if n == num:
        print("Congragulations!! , You have guessed the correct number : {num}")
        break
    elif n > num:
        print(f"You have entered a higher number, Try a number less than {n}")
        attempts -= 1
    elif n < num:
        print(f"You have entered a lower number, Try a number more than {n}")
        attempts -= 1
if attempts > 0:
    print(f"Your score is {attempts} out of 5")
else:
    print(f"You are out of attempts, The number was {num}. Better luck next time!")