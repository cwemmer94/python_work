import random

secret_number = random.randint(1,100)
numTries = 0
print("Give me a number between 1 and 100, but you only have 10 tries!")
while numTries < 10:
    user_choice = int(input("> "))
    if user_choice > secret_number:
        print("That number is too high, try going lower!")
        numTries += 1
    elif user_choice < secret_number:
        print("That number is too low, try going higher!")
        numTries += 1
    else:
        print(f"Wow you got it right! The number was {secret_number}")
        break
else:
    print(f"Sorry the number was {secret_number}")
