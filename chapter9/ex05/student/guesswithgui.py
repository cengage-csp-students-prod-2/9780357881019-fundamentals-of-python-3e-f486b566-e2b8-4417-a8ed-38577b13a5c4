import tkinter as tk
import random

class GuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Guess the Number Game")
        
        self.target_number = random.randint(1, 100)
        self.guess = None
        
        self.label = tk.Label(master, text="Computer's Guess: ")
        self.label.pack()
        
        self.guess_label = tk.Label(master, text="")
        self.guess_label.pack()
        
        self.too_small_button = tk.Button(master, text="Too Small", command=self.too_small)
        self.too_small_button.pack()
        
        self.too_large_button = tk.Button(master, text="Too Large", command=self.too_large)
        self.too_large_button.pack()
        
        self.correct_button = tk.Button(master, text="Correct", command=self.correct)
        self.correct_button.pack()
        
        self.new_game_button = tk.Button(master, text="New Game", command=self.new_game)
        self.new_game_button.pack()
        
        self.start_game()

    def start_game(self):
        self.guess = random.randint(1, 100)
        self.guess_label.config(text=str(self.guess))
        self.too_small_button.config(state=tk.NORMAL)
        self.too_large_button.config(state=tk.NORMAL)
        self.correct_button.config(state=tk.NORMAL)

    def too_small(self):
        if self.guess < 100:
            self.guess += random.randint(1, 100 - self.guess) // 2
            self.guess_label.config(text=str(self.guess))
        else:
            self.end_game()

    def too_large(self):
        if self.guess > 1:
            self.guess -= random.randint(1, self.guess) // 2
            self.guess_label.config(text=str(self.guess))
        else:
            self.end_game()

    def correct(self):
        self.end_game()

    def end_game(self):
        self.too_small_button.config(state=tk.DISABLED)
        self.too_large_button.config(state=tk.DISABLED)
        self.correct_button.config(state=tk.DISABLED)

    def new_game(self):
        self.target_number = random.randint(1, 100)
        self.start_game()

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()