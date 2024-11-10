The Python Slots Game is a simple slot machine game written in Python. Players are given an initial balance, and they can place bets on each spin of the slot machine. The game features different symbols, each with its own payout multiplier. The goal is to match all three symbols in a row for a payout. The game continues until the player runs out of money or decides to quit.

## Features
Five Symbols: 🍒 (cherry), 🍉 (watermelon), 🍋 (lemon), 🔔 (bell), and ⭐ (star).
Payout Multiplier: Each symbol has its own payout multiplier, with stars offering the highest rewards.
Betting System: Players can place a bet, which is deducted from their balance. If they win, the payout is added back.
Replay Option: After each spin, players can choose to play again or exit.
Balance Tracking: Players can see their current balance and are informed of the result after each spin.
Symbols & Payouts
The following symbols are available in the game, each offering different payout multipliers:

Symbol	Payout Multiplier
🍒	3x
🍉	5x
🍋	7x
🔔	10x
⭐	20x
## How to Play
Start the Game: The game will prompt you to place your bet.
Place Your Bet: Input the amount you'd like to bet. Your balance must be sufficient to place the bet.
Spin the Reels: The slot machine will "spin" and show three symbols in a row.
Check the Results: If the three symbols match, you will win a payout based on the symbol. The payout will be added to your balance.
Play Again or Exit: After each spin, you can choose to play again or exit the game.
Instructions
Run the Game: Execute the Python script slots_game.py in your terminal or IDE.
Place Your Bet: When prompted, enter the amount you'd like to wager (must be a positive number and not greater than your balance).
Enjoy the Spin: After spinning, the result will be displayed. If you win, the payout is added to your balance.
Game Over: The game will end if your balance is 0, or if you choose to exit by entering 'N' when asked if you want to play again.
Example Gameplay
markdown
Copy code
*****************************
Welcome to the Python slots
Symbols: 🍒 🍉 🍋 🔔 ⭐
*****************************

Your current balance is $100
Place your bet amount: 10
spinning... 

**************
🍋 | 🍋 | 🍋
**************

Congratulations, you have won $70 

Do you want to play again (Y/N): Y
Your current balance is $160
Place your bet amount: 50
spinning... 

**************
🍒 | 🍉 | 🍒
**************

Sorry, you lost this round

Do you want to play again (Y/N): N
***********************************************
Game over! Your final balance is $110
***********************************************

## Requirements
Python 3.x
No additional libraries are required, as the game uses built-in Python functions.
Game Design
The core of the game is based on randomly selecting symbols for each "spin," which is done using Python’s random.choice() function. The player places a bet, which is deducted from their balance, and if they win, the payout is added to their balance. The game loops until the player’s balance reaches zero or they decide to quit.

## License
This game is provided for educational purposes and is free to use and modify.

Regards Sufyan!
