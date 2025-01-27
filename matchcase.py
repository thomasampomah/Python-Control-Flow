import random
secret_number = random.randint(1,5)
guess = int(input("guess a number from 1 to 5: "))
print(secret_number)


match secret_number:
    case 1:
        if guess == 1:
            print("congratulation")
        else:
            print("sorry, try again")
    case 2:
        if guess == 2:
            print("congratulation")
        else:
            print("sorry, try again")
    case 3: 
        if guess == 3:
            print("congralutions")
        else: 
            print("try again")
    case 4:
        if guess == 4:
            print("congratulation")
        else:
            print("try again")
    case 5:
        if guess == 5:
            print("congratulations")
        else:
            print("sorry, try again")
    case _:
        print("sorry, Enter a number between 1 and 5")