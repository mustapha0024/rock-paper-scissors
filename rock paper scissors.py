import random

print("Welcome to Rock, Paper, Scissors!")
choices = ["rock", "paper", "scissors"]

choice = input("Choose rock, paper, or scissors: ").lower()
computer_choice = random.choice(choices)

print("You chose:", choice)
print("Computer chose:", computer_choice)

if choice == computer_choice:
    print("It's a tie!")
elif (
    (choice == "rock" and computer_choice == "scissors")
    or (choice == "paper" and computer_choice == "rock")
    or (choice == "scissors" and computer_choice == "paper")
):
    print("You win!")
else:
    print("Computer wins!")