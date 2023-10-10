import tkinter as tk

# initialize instance variables
stones = [ 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
#         player 1             player 2
holes = [None for _ in range(14)]

root = tk.Tk()
root.title("Mancala")

# creates buttons visually representing holes
for i in range(2):
    for j in range(6):
        normalhole = tk.Button(root, text=stones[i*6 + j], height= 3, width=6)
        normalhole.grid(row=i, column=j+1, padx=5, pady=5)
        holes[ i*6 + j ] = normalhole
    mancala = tk.Button(root, text=stones[6+ i*6], height= 3, width=20)
    mancala.grid(row=0, column=7*i, padx=5, pady=5)
    holes[6 + i*6] = mancala

root.mainloop()