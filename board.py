import tkinter as tk

stones = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
holes = [None for _ in range(14)]

root = tk.Tk()
root.title("Mancala")

def click(index):
    return

# creates buttons visually representing holes
for i in range(2):
    for j in range(6):
        normalhole = tk.Button(root, text=stones[i*7 + j], height=3, width=6, command=lambda index=(i*7+j): click(index))
        normalhole.grid(row=i, column=j+1, padx=5, pady=5)
        holes[i*7 + j] = normalhole
    mancala = tk.Button(root, text=stones[6 + i*7], height=3, width=20)
    mancala.grid(row=0, column=7*i, padx=5, pady=5)
    holes[6 + i*7] = mancala


root.mainloop()