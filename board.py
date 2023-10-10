import tkinter as tk

holes = [None for _ in range(14)]

root = tk.Tk()
root.title("Mancala")

def click(index):
    pickedup = holes[index.cget("name")]
    print(pickedup)
    return

# creates buttons visually representing holes
for i in range(2):
    for j in range(6):
        normalhole = tk.Button(root, text="4", height=3, width=6, command=lambda index=(i*7+j): click(index))
        normalhole.grid(row=i, column=j+1, padx=5, pady=5)
    mancala = tk.Button(root, text="0", height=3, width=20)
    mancala.grid(row=0, column=7*i, padx=5, pady=5)


root.mainloop()