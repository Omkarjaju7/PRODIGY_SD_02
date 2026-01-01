import tkinter as tk
import random

number = random.randint(1, 100)
attempts = 0

def check():
    global attempts
    guess = int(entry.get())
    attempts += 1

    if guess > number:
        result.set("Too High!")
    elif guess < number:
        result.set("Too Low!")
    else:
        result.set(f"Correct! Attempts: {attempts}")

root = tk.Tk()
root.title("Guessing Game")

tk.Label(root, text="Guess number (1–100)").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Check", command=check).pack()
result = tk.StringVar()
tk.Label(root, textvariable=result).pack()

root.mainloop()
