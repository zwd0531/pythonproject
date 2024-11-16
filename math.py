import random

def guess_number():
    random_number = random.randiant(1,100)
    print("I have generated a number")

    while True:
        user_guessed_number =int(input("please guess a number"))
        if user_guessed_number > random_number:
            print("too large!")
        elif user_guessed_number < random_number:
            print("Too small!")    
        else:
            print("You are correct")
