import random

def spin_row():
    symbols = ["🍒" ,"🍉" ,"🍋", "🔔" ,"⭐"]
    return [ random.choice(symbols) for _ in range(3)]


def print_row(row):
    print(" | ".join(row)) 


def get_payout(row,bet):
    if row[0] == row[1] == row[2]:

        if row[0] == "🍒":
            return  bet * 3
        
        elif row[0] == "🍉":
            return  bet * 5
        
        elif row[0] == "🍋":
            return  bet * 7
                
        elif row[0] == "🔔":
            return  bet * 10
        
        elif row[0] == "⭐":
            return  bet * 20

    return 0

    
def main():
    
    print("*****************************")
    print("Welcome to the Python slots")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("***************************** \n")

    balance = 100

    while balance > 0:
        print(f"Your current balance is ${balance}")
          
        bet = input("Place your bet amount: ")

        if bet == "":
            print("Enter a valid amount \n")
            continue
        
        if not bet.isdigit():
            print("Please enter a valid number \n")
            continue

        bet = int(bet)

        if bet < 0 :
            print("Bet canot be less than 0 \n")
            continue

        if bet > balance:
            print("Insufficient amount of funds \n")
            continue

        balance -= bet 


        row = spin_row()
        print("spinning... \n")

        print("**************")
        print_row(row)
        print("**************")


        payout = get_payout(row,bet)

        if payout > 0:
            print(f"congratulation you have won ${payout} \n")
        else:
            print("Sorry you lost this round \n ")
        balance += payout

        choice = input("Do you wanna play again (Y/N): ").capitalize()
        if choice != "Y":
            break


    print("\n***********************************************")        
    print(f"Game over! Your final balance is ${balance}")
    print("***********************************************")

if __name__ == "__main__":
    main()