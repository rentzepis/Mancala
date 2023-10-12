
# idea for player turns
def holeClick(self, i):
    if player1turn == True:
        for x in range (6):
            if i == x:
                pickedup = int(self.buttons[i].cget("text"))
                self.buttons[i].config(text=0)
                for x in range(pickedup):
                    i = i + 1
                    self.incrementStoneCount(i)
            else:
                tk.messagebox.showerror(title='error', message='pick a hole in your own side')

                break

    if player2turn == True:
        for x in range (7,14):
            if i == x:
                pickedup = int(self.buttons[i].cget("text"))
                self.buttons[i].config(text=0)
                for x in range(pickedup):
                    i = i + 1
                    self.incrementStoneCount(i)
            else:
                tk.messagebox.showerror(title='error', message='pick a hole in your own side')
                break