import random

options = ("rock", "paper", "scissors");
playing = True;

while playing:
    player = None;
    computer = random.choice(options);

    while player not in options:
        player = input("Enter your choice (rock, paper, scissors) : ").lower();

    print(f"Player: {player}");
    print(f"Computer: {computer}");

    if player == computer:
        print("Tie!!!");
    elif player == "rock" and computer == "scissors":
        print("You win!");
    elif player == "scissors" and computer == "paper":
        print("You win!");
    elif player == "paper" and computer == "rock":
        print("You win!");
    else:
        print("You lose!");

    if not input("Play again? (y/n): ").lower() == "y":
        playing=False;

print();
print("Thanks for playing!!!")