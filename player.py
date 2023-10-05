import random as random
import tkinter as tk
from tkinter import simpledialog


Root = tk.Tk()
Root.withdraw()

player1Name = simpledialog.askstring(title="Welcome", prompt='First player type your name: ')

print("Hello", player1Name)

player2Name = simpledialog.askstring(title="Welcome", prompt='Second player type your name: ')

print("Hi", player2Name)

print("Now we will flip a coin to decide who goes first")
print("Ready...")
print("3")
print("2")
print("1")

coinFlip = random.randint(0, 1)
if coinFlip == 0 :
    P
