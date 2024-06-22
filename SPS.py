import tkinter as tk
from random import choice

class RockPaperScissors:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Rock, Paper, Scissors")
        self.window.geometry("400x300")

        self.player_score = 0
        self.computer_score = 0

        self.header_label = tk.Label(self.window, text="Rock, Paper, Scissors", font=("Arial", 24, "bold"))
        self.header_label.pack(pady=20)

        self.score_frame = tk.Frame(self.window)
        self.score_frame.pack()

        self.player_score_label = tk.Label(self.score_frame, text="Player Score: 0", font=("Arial", 18))
        self.player_score_label.pack(side=tk.LEFT, padx=20)

        self.computer_score_label = tk.Label(self.score_frame, text="Computer Score: 0", font=("Arial", 18))
        self.computer_score_label.pack(side=tk.RIGHT, padx=20)

        self.result_label = tk.Label(self.window, text="", font=("Arial", 18), wraplength=350)
        self.result_label.pack(pady=20)

        self.choice_frame = tk.Frame(self.window)
        self.choice_frame.pack()

        self.rock_button = tk.Button(self.choice_frame, text="Rock", command=lambda: self.play("rock"), width=10, height=2)
        self.rock_button.pack(side=tk.LEFT, padx=10)

        self.paper_button = tk.Button(self.choice_frame, text="Paper", command=lambda: self.play("paper"), width=10, height=2)
        self.paper_button.pack(side=tk.LEFT, padx=10)

        self.scissors_button = tk.Button(self.choice_frame, text="Scissors", command=lambda: self.play("scissors"), width=10, height=2)
        self.scissors_button.pack(side=tk.LEFT, padx=10)

        self.window.update_idletasks()  # Update the window to get the actual width
        self.result_label.config(wraplength=self.window.winfo_width() - 20)  # Set the wraplength to the window width

    def play(self, player_choice):
        choices = ["rock", "paper", "scissors"]
        computer_choice = choice(choices)

        if player_choice == computer_choice:
            result = "It's a tie!"
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            result = "Player wins!"
            self.player_score += 1
        else:
            result = "Computer wins!"
            self.computer_score += 1

        self.result_label.config(text=f"Player: {player_choice}, Computer: {computer_choice}, {result}")
        self.player_score_label.config(text=f"Player Score: {self.player_score}")
        self.computer_score_label.config(text=f"Computer Score: {self.computer_score}")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = RockPaperScissors()
    game.run()