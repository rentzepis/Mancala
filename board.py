import tkinter as tk
from player import *
class Board:
    global stones
    stones = [ 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
    global holes
    holes = [None for _ in range(14)]

    root = tk.Tk()
    root.title("Mancala")

def changeHoleStones(self, index, num):
    stones[index] = stones[index] + num

# creates buttons visually representing holes
for i in range(2):
    for j in range(6):
        normalhole = tk.Button(root, text=stones[i*7 + j], height=3, width=6)
        normalhole.grid(row=i, column=j+1, padx=5, pady=5)
        holes[i*7 + j] = normalhole
    mancala = tk.Button(root, text=stones[6 + i*7], height=3, width=20)
    mancala.grid(row=0, column=7*i, padx=5, pady=5)
    holes[6 + i*7] = mancala

    root.mainloop()

class Main:
    x=3