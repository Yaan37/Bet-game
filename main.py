import random

options = ("rock", "paper", "scissors")
running = True

print("🎮 Welcome to the Rock, Paper, Scissors Game! 🎉")

while running:
    # Computer's choice
    computer = random.choice(options)
    player = None

    # Input validation
    while player not in options:
        player = input("🪨  📃 ✂️ Enter a choice (rock, paper, scissors): ").lower()

        if player not in options:
            print("❌ Invalid choice. Please choose 🪨 rock, 📃 paper, or ✂️ scissors.\n")

    # Display choices
    print(f"\n🧍 Player: {player} \n🤖 Computer: {computer}")

    # Determine the winner
    if player == computer:
        print("⭐ It's a tie! 🎲\n")
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        print("🎉 You win! 🏆\n")
    else:
        print("😞 You lose! Better luck next time! 💔\n")

    # Replay option
    play_again = input("🔁 Do you want to play again? (Y/N): ").lower()
    if not play_again.startswith("y"):
        running = False

print("👋 Thanks for playing! 🌟")
