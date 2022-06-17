import random


rps = ["rock", "paper", "scissors"]

guess = input("Enter a guess(rock, paper, scissors): ")

rgess = random.choice(rps)
print(rgess)

if guess ==  rgess :
    print("Draw")
elif guess == "rock" and rgess == "scissors":
    print("Well done")
elif guess == "paper" and rgess == "rock":
    print("Well done")
elif guess == "scissors" and rgess == "paper":
    print("Well done")

else:
    print("Mabye next time")








