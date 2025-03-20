from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "Congratulations You win!"
    else:
        return "This time Computer wins!"

@app.route('/', methods=['GET', 'POST'])
def play_game():
    if 'player_score' not in session:
        session['player_score'] = 0
        session['computer_score'] = 0
        session['game_history'] = []
        session['player_name'] = ''

    if request.method == 'POST':
        if not session['player_name']:
            session['player_name'] = request.form['player_name']
        
        user_choice = request.form['choice']
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)

        if result == "Congratulations You win!":
            session['player_score'] += 1
        elif result == "This time Computer wins!":
            session['computer_score'] += 1

        session['game_history'].append((session['player_score'], session['computer_score'], user_choice, computer_choice, result))
        if len(session['game_history']) > 5:
            session['game_history'].pop(0)

        if len(session['game_history']) == 5:
            if session['player_score'] > session['computer_score']:
                winner = f"{session['player_name'].upper()} IS THE WINNER!"
            elif session['computer_score'] > session['player_score']:
                winner = "COMPUTER IS THE WINNER!"
            else:
                winner = f"WOW, IT'S A TIE! between {session['player_name'].upper()} and COMPUTER"
            return render_template('result.html', player_name=session['player_name'], user_choice=user_choice, computer_choice=computer_choice, result=result, player_score=session['player_score'], computer_score=session['computer_score'], game_history=session['game_history'], winner=winner)

        return render_template('result.html', player_name=session['player_name'], user_choice=user_choice, computer_choice=computer_choice, result=result, player_score=session['player_score'], computer_score=session['computer_score'], game_history=session['game_history'])

    return render_template('index.html', player_name=session['player_name'])

if __name__ == "__main__":
    print("Starting Flask app on http://127.0.0.1:5000/")
    app.run(debug=True)
