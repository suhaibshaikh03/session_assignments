import random

print("Welcome to High-Low Game!")
print("-------------------------")
counter = 0
round_num = 1

def abc():
    global counter, round_num
    user = random.randint(1, 100)
    comp = random.randint(1, 100)
    
    print(f"\nRound {round_num}")
    print(f"Your number is: {user}")
    print(f"Computer's number is: {comp}")
    
    high_low = input("Do you think your number is higher or lower than the computer's (h/l)?\n")

    if high_low == 'h':
        if user > comp:
            print(f"You were right! The computer's number was {comp}")
            counter += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {comp}")
    elif high_low == 'l':
        if user < comp:
            print(f"You were right! The computer's number was {comp}")
            counter += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {comp}")
    
    print(f"Your score is: {counter}")
    round_num += 1

while round_num <= 3:
    abc()

print("Game Over!")
