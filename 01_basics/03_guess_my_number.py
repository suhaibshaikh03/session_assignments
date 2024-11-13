import random
allowed_attempts : int = 5
user_attempts : int = 0
while user_attempts < allowed_attempts:
    print(f"Attempts left : {allowed_attempts-user_attempts}")
    num = random.randint(1,99)
    num1 : int = int(input("Take a random guess from 1 to 99\n"))
    user_attempts += 1
    if num1 > 99 or num1 < 1:
        print("enter a valid number")
    else:
        if num1 == num:
            print("you guessed it right")
            break
        elif num1>num:
            print("your guess is too high")
            print("enter a new number")
        elif num1<num:
            print("your guess is too low")
            print("enter a new number") 

if (user_attempts == allowed_attempts):
    print("game over")
