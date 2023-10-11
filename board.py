import tkinter as tk

class ButtonGrid:
    def __init__(self, root, p1, p2):
        self.player1 = p1
        self.player2 = p2


        self.buttons = []

        mancala = tk.Button(root, text='0', pady=20, command=lambda i=0: self.holeclick(i))
        mancala.grid(row=0, column=0, padx=5, pady=5, rowspan=2)
        self.buttons.append(mancala)

        for i in range(1,7):
            button = tk.Button(root, text='4', command=lambda i=i: self.holeclick(i))
            button.grid(row=0, column=i, padx=5, pady=5)
            self.buttons.append(button)

        mancala = tk.Button(root, text='0', pady=20, command=lambda i=7: self.holeclick(i))
        mancala.grid(row=0, column=8, padx=5, pady=5, rowspan=2)
        self.buttons.append(mancala)

        for i in range(13,7,-1):
            button = tk.Button(root, text='4', command=lambda i=i: self.holeclick(i))
            button.grid(row=1, column=14-i, padx=5, pady=5)
            self.buttons.append(button)

    def holeclick(self, i):
        pickedup = int(self.buttons[i].cget("text"))
        print(f'Button {pickedup} clicked')

def main():
    import tkinter as tk
    import random as random

    root = tk.Tk()
    root.geometry("800x800")

    prompt = tk.Label(text="First player's name")
    prompt.pack()
    player1name = tk.Entry(root)

    prompt.config(text="Second player's name")
    player2name = tk.Entry(root)


    print("Hi", player2name)

    print("Now we will flip a coin to decide who goes first")
    print("Ready...")
    print("3")
    print("2")
    print("1")

    coinFlip = random.randint(0, 1)
    if coinFlip == 0:
        player1 = player1name
        player2 = player2name
    else:
        player1 = player2name
        player2 = player1name

    root = tk.Tk()
    app = ButtonGrid(root, "a", "b")
    root.mainloop()

if __name__ == "__main__":
    main()