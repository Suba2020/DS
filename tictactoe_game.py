# Tic Tac Toe game program using Tkinter module in Python
# Python Project by Suba on 26Feb2021, Optimised code using list (269 lines reduced to 85 lines)
# Reference: https://data-flair.training/blogs

from functools import partial
from tkinter import *
import tkinter.messagebox as msg
gui = Tk()
gui.title('TIC_TAC_TOE : TWO PLAYER GAME by Suba2020')

# labels
Label(gui, text="Player1 : X", font="Verdana 15").grid(row=0, column=1)
Label(gui, text="Player2 : O", font="Verdana 15").grid(row=0, column=2)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#button_list=['0']*10
button_list=['0']

# for player1 sign = X and for player2 sign = Y
mark = ''

# counting the no. of click
count = 0
panels = ["panel"] * 10

#To Check the winner
def win(panels, sign):
    return ((panels[1] == panels[2] == panels[3] == sign)
            or (panels[1] == panels[4] == panels[7] == sign)
            or (panels[1] == panels[5] == panels[9] == sign)
            or (panels[2] == panels[5] == panels[8] == sign)
            or (panels[3] == panels[6] == panels[9] == sign)
            or (panels[3] == panels[5] == panels[7] == sign)
            or (panels[4] == panels[5] == panels[6] == sign)
            or (panels[7] == panels[8] == panels[9] == sign))

# Check which button clicked
def click_check(digit):
    global count, mark, digits

    if digit in digits:
        digits.remove(digit)
        #player1 will play if the value of count is even and for odd player2 will play
        if count % 2 == 0:
            mark = 'X'
            panels[digit] = mark
        elif count % 2 != 0:
            mark = 'O'
            panels[digit] = mark

        button_list[digit].config(text=mark)
        count = count + 1
        sign = mark

        if (win(panels, sign) and sign == 'X'):
            msg.showinfo("Result", "Player1 wins")
            gui.destroy()
        elif (win(panels, sign) and sign == 'O'):
            msg.showinfo("Result", "Player2 wins")
            gui.destroy()

    #if count is greater then 8 then the match has been tied
    if (count > 8 and win(panels, 'X') == False and win(panels, 'O') == False):
        msg.showinfo("Result", "Match Tied")
        gui.destroy()


#define buttons
def create_buttons():
    row_val=1
    for d in digits:
        button = Button(gui, width=15, height=7, font=('Verdana 10 bold'), command=partial(click_check, d))
        if (d%3==0):
            col_val = 3
            row_val = d//3
        else:
            col_val = d%3
            row_val = 1 + d//3
        button.grid(row=row_val, column=col_val)
        button_list.append(button)

# Create the required buttons and invoke GUI for play
create_buttons()
gui.mainloop()
