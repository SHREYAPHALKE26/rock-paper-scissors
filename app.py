from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Initialize scores
user_score = 0
computer_score = 0

# Define the game logic
def determine_winner(user_choice, computer_choice):
    global user_score, computer_score
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "STONE" and computer_choice == "SCISSORS") or \
         (user_choice == "SCISSORS" and computer_choice == "PAPER") or \
         (user_choice == "PAPER" and computer_choice == "STONE"):
        user_score += 1
        return "You win!"
    else:
        computer_score += 1
        return "Computer wins!"

# Home route
@app.route("/", methods=["GET", "POST"])
def index():
    global user_score, computer_score
    user_choice = None
    computer_choice = None
    result = None
    username = None

    if request.method == "POST":
        if "username" in request.form:
            # Get the username from the form
            username = request.form.get("username")
        else:
            # Handle the game logic
            username = request.form.get("username_hidden")  # Retrieve username from hidden input
            user_choice = request.form.get("choice")
            computer_choice = random.choice(["STONE", "PAPER", "SCISSORS"])
            result = determine_winner(user_choice, computer_choice)

    return render_template("index.html", 
                           user_choice=user_choice, 
                           computer_choice=computer_choice, 
                           result=result,
                           user_score=user_score,
                           computer_score=computer_score,
                           username=username)

# Reset scores
@app.route("/reset", methods=["POST"])
def reset_scores():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)