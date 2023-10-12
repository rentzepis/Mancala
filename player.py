import random as random
import tkinter as tk
from tkinter import simpledialog
from time import *

Root = tk.Tk()
Root.withdraw()

player1Name = simpledialog.askstring(title="Welcome", prompt='First player type your name: ')

player2Name = simpledialog.askstring(title="Welcome", prompt='Second player type your name: ')


coinFlip = random.randint(0, 2)
if coinFlip == 0:
    player1 = player1Name
    player2 = player2Name
else:
    player1 = player2Name
    player2 = player1Name

print(player1, ", You go first!")
