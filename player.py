import random as rand
import tkinter as tk
from tkinter import simpledialog


Root = tk.Tk()

Root.withdraw()
# the input dialog
player1Name = simpledialog.askstring(title="Welcome", prompt='First player type your name: ')

print("Hello", player1Name)

player2Name = simpledialog.askstring(title="Welcome", prompt='Second player type your name: ')

print("Hi", player2Name)

print("Now we will flip a coin to decide who goes first")
print("Ready...")
print("3")
print("2")
print("1")
