import tkinter as tk
from time import sleep

class ButtonGrid:
    # sets up board
    # root is window to be written into (Tk object), p1 is player 1's name (str), p2 is player 2's name (str)
    def __init__(self, root, p1, p2):
        self.player1 = p1
        self.player2 = p2
        self.buttons = []

        # player 1's row
        for i in range(6):
            button = tk.Button(root, text='4', fg="red", command=lambda i=i: self.holeClick(i))
            button.grid(row=0, column=i+1, padx=5, pady=5)
            self.buttons.append(button)
        # player 1's mancala
        mancala = tk.Button(root, text='0', pady=20, fg="red")
        mancala.grid(row=0, column=8, padx=5, pady=5, rowspan=2)
        self.buttons.append(mancala)
        # player 2's row (sets up backwards in order to continue flow of play)
        for i in range(7,13):
            button = tk.Button(root, text='4', fg="blue", command=lambda i=i: self.holeClick(i))
            button.grid(row=1, column=13-i, padx=5, pady=5)
            self.buttons.append(button)
        # player 2's mancala
        mancala = tk.Button(root, text='0', pady=20, fg="blue")
        mancala.grid(row=0, column=0, padx=5, pady=5, rowspan=2)
        self.buttons.append(mancala)

    # returns the # of stones in the specified hole
    def getStoneCount(self,i):
        holeCount = int(self.buttons[i].cget("text"))
        return holeCount

    def incrementStoneCount(self, i):
        old = self.getStoneCount(i)
        self.buttons[i].config(text=(old+1))

    def holeClick(self, i):
        turn = 1
        if (turn==1 and i not in range(6)) or (turn==2 and i not in range(7,13)):
            tk.messagebox.showerror(title='error', message='pick a hole in your own side')
            return "error"

        pickedup = self.getStoneCount(i)

        while pickedup != 0:
            self.buttons[i].config(text=0)
            while pickedup != 0:
                i = (i + 1)%14
                pickedup = pickedup-1
                print(i, ":", self.getStoneCount(i), "pickedup =", pickedup)
                if pickedup == 0:
                    pickedup = self.getStoneCount(i)
                    self.incrementStoneCount(i)
                    break
                self.incrementStoneCount(i)
                sleep(0.25)

            print(pickedup)






# asks for a player's name and returns that string
def playerNameDialog(playernumber):
    import tkinter as tk
    from tkinter import simpledialog

    name = simpledialog.askstring(title="Welcome", prompt=f'{playernumber} player name: ')
    return name


#runs the actual code
def main():
    import tkinter as tk
    import random as random

    player1name = playerNameDialog("First")
    player2name = playerNameDialog("Second")

    print("Hi", player2name)

    tk.messagebox.showinfo(title='Mancala', message="Now we will flip a coin to decide who goes first!")
    print("Ready...")
    print("3")
    print("2")
    print("1")

    # random coin flip determines first player
    coinFlip = random.randint(0, 2)
    if coinFlip == 0:
        player1 = player1name
        player2 = player2name
    else:
        player1 = player2name
        player2 = player1name

    root = tk.Tk()
    ButtonGrid(root, "a", "b")
    player1side = tk.Label(text=f"{player1}")
    player1side.grid(row=2)

    root.mainloop()

if __name__ == "__main__":
    main()