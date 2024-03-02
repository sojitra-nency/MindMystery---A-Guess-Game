import random
import math

lower = int(input("Enter starting range: "))
upper = int(input("Enter ending range: "))

chances = int(math.log(upper - lower+1, 2))
print(f" You got {chances} chances to guess it right!")

target = random.randint(lower, upper+1)
user_input = int(input("Enter a number: "))

count = 0
while(user_input!=target):
    count += 1
    if user_input > target:
        print("Too High!!")
    elif user_input < target:
        print("Too Low!!")
    if count >= chances:
        print(f"Correct Number was {target}.")
        print("Better Luck Next Time!")
        break
    user_input = int(input("Enter a number: "))

else:
    print("You guessed it right! Congrats!")