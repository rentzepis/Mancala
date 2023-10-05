import tkinter as tk

# initialize instance variables
stones = [ 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
holes = [None for _ in range(14)]
#         player 1             player 2

root = tk.Tk()
root.title("Mancala")

# creates buttons visually representing holes
for i in range(2):
    for j in range(6):
        normalhole = tk.Button(root, text=stones[i*6 + j], height= 3, width=6)
        normalhole.grid(row=j+2, column=i, padx=5, pady=5)
        holes[ i*6 + j ] = normalhole
    mancala = tk.Button(root, text=stones[i*6 + j], height= 3, width=12)
    mancala.grid(row=2 + 6*(i), column=0, padx=5, pady=5)
    holes[6 + i*6]

root.mainloop()