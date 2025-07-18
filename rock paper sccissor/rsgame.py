import random

# Score tracking
user_score = 0
computer_score = 0
choices = ["rock", "paper", "scissors"]

def get_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

# Game loop
while True:
    print("\nChoose one: rock, paper, or scissors")
    user_choice = input("Your choice: ").lower()

    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    winner = get_winner(user_choice, computer_choice)

    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    # Show scores
    print(f"Score → You: {user_score} | Computer: {computer_score}")

    # Play again?
    play_again = input("\nDo you want to play another round? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
