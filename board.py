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

    def winner(self):
        score1 = self.getStoneCount(6)
        score2 = self.getStoneCount(13)
        #player 1's score is bigger
        if score1 > score2:
            tk.messagebox.showinfo(title='Winner', message=f"{self.player1} wins!")
        else:
            tk.messagebox.showinfo(title='Winner', message=f"{self.player2} wins!")

    #stealing mechanism when one side is fully empty
    def stealSide(self):
        sum1 = 0
        sum2 = 0

        #checks player sides to see if either has no stones
        for x in range(0,6):
            sum1 += self.getStoneCount(x)
            sum2 += self.getStoneCount(x+7)

        # player 1 or 2 side no stones --> means one player wins, adds the
        # score of the other player's holes to their mancala
        if sum1 == 0:
            self.buttons[6].config(text=(self.getStoneCount(6)+sum2))
            self.winner()
        elif sum2 == 0:
            self.buttons[13].config(text=(self.getStoneCount(13)+sum1))
            self.winner()


    #checks if a player has cleared their side of the board and who won
    def checkWin(self, turn):
        sum= 0
        #adding up stones in player1 row
        for x in range (0,5):
            sum =+ self.buttons[i]
            i= i+1
        #adding up stones in player2 row
        for x in range (7,13):
            sum =+ self.buttons[i]
            i= i+1
        #checks addtion of stones in each players row
        if sum == 0:
            Win = True

    #the function that places stones based on which hole you click and how many stones it was
    def holeClick(self, i):
        if self.player1turn: # if it is player 1's turn
            turn = 1
        else:
            turn = 2

        pickedup = self.getStoneCount(i)
        #while there are still stones left to be distributed
        while pickedup != 0:
            self.buttons[i].config(text=0)
            #inner loop for distributing stones (allows for chained pickups)
            while pickedup != 0:
                i = (i+1)%14
                # skips opposing player's mancala
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
                sleep(0.1)

        #board shows which players turn it is in their assigned color
        if self.label.cget("text") == f"{self.player1}'s turn":
            self.label.config(text=f"{self.player2}'s turn", fg="blue")
        else:
            self.label.config(text=f"{self.player1}'s turn", fg="green")
        self.player1turn = not self.player1turn

        self.stealSide()

        return False


# asks for a player's name and returns that string
def playerNameDialog(playernumber):
    from tkinter import simpledialog
    return simpledialog.askstring(title="Welcome", prompt=f'{playernumber} player name: ')


#handler to initialize board and players
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

#runs main code
if __name__ == "__main__":
    main()