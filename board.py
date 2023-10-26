import tkinter as tk
import tkinter.font as font
from time import sleep

class ButtonGrid:
    # sets up the game board
    # root is window to be written into (Tk object), p1 is player 1's name (str), p2 is player 2's name (str)
    def __init__(self, root, p1, p2):
        self.player1 = p1
        self.player2 = p2
        self.buttons = []

        # player turn label and color
        myFont = font.Font(size=30)
        self.label = tk.Label(root, text=f"{self.player1}'s turn", fg="green", font=myFont, pady=6)
        self.label.grid(row=3, columnspan=9)
        
        self.player1turn = True

        # player 1's row is top row and green
        for i in range(6):
            button = tk.Button(root, text='4', fg="green", height=2, width=5, font=myFont, command=lambda i=i: self.holeClick(i))
            button.grid(row=0, column=i+1, padx=5, pady=5)
            self.buttons.append(button)
        # player 1's mancala
        mancala = tk.Button(root, text='0', pady=20, fg="green", height=4, width=5, font=myFont)
        mancala.grid(row=0, column=8, padx=5, pady=5, rowspan=2)
        self.buttons.append(mancala)
        # player 2's row (sets up backwards in order to continue flow of play)
        for i in range(7,13):
            button = tk.Button(root, text='4', fg="blue", height=2, width=5, font=myFont, command=lambda i=i: self.holeClick(i))
            button.grid(row=1, column=13-i, padx=5, pady=5)
            self.buttons.append(button)
        # player 2's mancala
        mancala = tk.Button(root, text='0', pady=20, fg="blue", height=4, width=5, font=myFont)
        mancala.grid(row=0, column=0, padx=5, pady=5, rowspan=2)
        self.buttons.append(mancala)


    # returns the # of stones in the specified hole
    def getStoneCount(self,i):
        holeCount = int(self.buttons[i].cget("text"))
        return holeCount

    def incrementStoneCount(self, i):
        old = self.getStoneCount(i)
        self.buttons[i].config(text=(old+1))

    def checkWin(self, turn):
        sum= 0
        for x in range (0,5):
            sum =+ self.buttons[i]
            i= i+1
        for x in range (7,13):
            sum =+ self.buttons[i]
            i= i+1
        if sum == 0
            Win = True
    def holeClick(self, i):
        if self.player1turn: # if it is player 1's turn
            turn = 1
        else:
            turn = 2

        #if (turn==1 and i not in range(6)) or (turn==2 and i not in range(7,13)) or i==6 or i ==13:
        #    tk.messagebox.showerror(title='error', message='Please pick a valid hole.')
        #    return "error"

        pickedup = self.getStoneCount(i)

        while pickedup != 0:
            self.buttons[i].config(text=0)
            while pickedup != 0:
                i = (i+1)%14
                #will help when making the code wrap through the array
                if (i == 13 and turn == 1) or (i == 6 and turn == 2):

                    i = i + 1
                    continue

                pickedup = pickedup-1


                # runs out of stones
                if pickedup == 0:
                    # if runs out of stones on a mancala
                    if (i == 6 and turn == 1) or (i == 13 and turn == 2):
                        self.incrementStoneCount(i)
                        return True
                    pickedup = self.getStoneCount(i)
                    break
                self.incrementStoneCount(i)

                sleep(0.2)

        #board shows which players turn it is in their assigned color
        if self.label.cget("text") == f"{self.player1}'s turn":
            self.label.config(text=f"{self.player2}'s turn", fg="blue")
        else:
            self.label.config(text=f"{self.player1}'s turn", fg="green")
        self.player1turn = not self.player1turn
        return False




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

    tk.messagebox.showinfo(title='Mancala', message="Now we will flip a coin to decide who goes first!")

    # random coin flip determines first player
    coinFlip = random.randint(0, 2)
    if coinFlip == 0:
        player1 = player1name
        player2 = player2name
    else:
        player1 = player2name
        player2 = player1name

    tk.messagebox.showinfo(title='Mancala', message=f"{player1} starts!")

    root = tk.Tk()
    ButtonGrid(root, player1, player2)

    root.mainloop()

if __name__ == "__main__":
    main()