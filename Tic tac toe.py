from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox

def click_button(id):
    global player1
    global player2
    global active_player
    if active_player == 1:
        set_layout(id, 'X')
        player1.append(id)
        active_player = 2
    else:
        set_layout(id, 'O')
        player2.append(id)
        active_player = 1
    winner = choose_winner()
    if winner == 0:
        check_draw()
    elif winner == 1:
        messagebox.showinfo('Winner', f'{name1} is the winner')
        window.quit()
    elif winner == 2:
        messagebox.showinfo('Winner', f'{name2} is the winner')
        window.quit()

def set_layout(id, symbol):
    button = buttons[id - 1]
    button.config(text=symbol, state=DISABLED)

def choose_winner():
    winner = 0
    winning_conditions = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
                          [1, 4, 7], [2, 5, 8], [3, 6, 9],
                          [1, 5, 9], [3, 5, 7]]
    
    for condition in winning_conditions:
        if all(position in player1 for position in condition):
            winner = 1
        elif all(position in player2 for position in condition):
            winner = 2

    return winner

def check_draw():
    if len(player1) + len(player2) == 9:
        messagebox.showinfo('Draw', 'It\'s a draw!')
        window.quit()

player1 = []
player2 = []
active_player = 1

window = Tk()
name1 = simpledialog.askstring('Name', 'Name of player 1', parent=window)
name2 = simpledialog.askstring('Name', 'Name of player 2', parent=window)

window.title("Tic-Tac-Toe")
window.resizable(True, True) 

buttons = []
for i in range(9):
    button = Button(window, height=3, width=7, font=("Helvetica", 24), command=lambda i=i: click_button(i + 1))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

window.mainloop()
