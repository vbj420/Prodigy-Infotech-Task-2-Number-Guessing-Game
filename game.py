import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")
        self.master.geometry("400x300")
        self.master.configure(bg="black")

        # Initialize game variables
        self.random_number = random.randint(0, 1000)
        self.attempts = 0
        self.incorrect_count = 0

        # Create GUI elements
        self.label = tk.Label(self.master, text="Guess the number:", bg="gray", fg="white")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.master)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.check_guess_enter)

        self.guess_button = tk.Button(self.master, text="Submit Guess", command=self.check_guess)
        self.guess_button.pack(pady=10)

        self.attempts_label = tk.Label(self.master, text=f"Attempts: {self.attempts}", bg="gray", fg="white")
        self.attempts_label.pack(pady=10)

    def check_guess(self, event=None):
        guess = self.entry.get()
        if guess.isdigit():
            guess = int(guess)

            if guess > 0:
                self.attempts += 1
                self.update_attempts_label()

                if guess == self.random_number:
                    messagebox.showinfo("Congratulations!", f"You guessed the number in {self.attempts} attempts.")
                    self.master.destroy()
                else:
                    self.incorrect_count += 1
                    self.display_hint()

                    if self.incorrect_count ==25:
                        
                        messagebox.showinfo("Game Over", "You have exceeded the maximum number of attempts. The game is over.")
                        
                        self.master.destroy()
            else:
                messagebox.showwarning("Invalid Input", "Please enter a number greater than 0.")
        else:
            messagebox.showwarning("Invalid Input", "Please enter a valid number.")

    def check_guess_enter(self, event):
        self.check_guess()

    def display_hint(self):
        range_start = max(0, self.random_number - 100)
        range_end = min(1000, self.random_number + 100)

        if self.incorrect_count == 5:
            range_start = self.random_number//100 *100
            range_end = range_start+100
            messagebox.showinfo("Hint", f"Hint: The number is in the range {range_start} to {range_end}")
        elif self.incorrect_count == 10:
            range_start = self.random_number//50 * 50
            range_end = range_start + 50
            messagebox.showinfo("Hint", f"Hint: The number is in the range {range_start} to {range_end}")
        elif self.incorrect_count == 15:
            range_start = self.random_number//10 * 10
            range_end = range_start + 10
            messagebox.showinfo("Hint", f"Hint: The number is in the range {range_start} to {range_end}")

    def update_attempts_label(self):
        self.attempts_label.config(text=f"Attempts: {self.attempts}")

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
