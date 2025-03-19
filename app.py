import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_user_choice():
    user_input = input("Enter your choice (rock, paper, or scissors): ").lower()
    while user_input not in ["rock", "paper", "scissors"]:
        user_input = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
    return user_input

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "Congratulations You win!"
    else:
        return "This time Computer wins!"

def play_game():
    print("\n\nWelcome to Rock-Paper-Scissors! Game\n\n")
    player_name = input("Enter your good name: ")
    player_score = 0
    computer_score = 0
    game_history = []
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"{player_name} chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        if result == "Congratulations You win!":
            player_score += 1
        elif result == "This time Computer wins!":
            computer_score += 1
        game_history.append((player_score, computer_score, user_choice, computer_choice, result))
        if len(game_history) > 5:
            game_history.pop(0)
        print(f"{player_name}'s score: {player_score}")
        print(f"Computer score: {computer_score}")
        print(f"Last {len(game_history)} Games:")
        for i, (p_score, c_score, u_choice, c_choice, res) in enumerate(game_history, 1):
            if "tie" in res.lower():
                print(f"Game {i}: GREAT GAME ITS A TIE! {player_name} and Computer both chose {u_choice}")
            else:
                print(f"Game {i}: {player_name} - {p_score}, Computer - {c_score}")
        if len(game_history) == 5:
            if player_score > computer_score:
                print(f"\n\n{player_name.upper()} IS THE WINNER!\n\n")
            elif computer_score > player_score:
                print("\n\nCOMPUTER IS THE WINNER!\n\n")
            else:
                print(f"\n\nWOW, IT'S A TIE! between {player_name.upper()} and COMPUTER \n\n")
            break
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    play_game()