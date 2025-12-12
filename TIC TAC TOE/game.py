from tkinter import *
import random

def next_turn(row, column):
    global player
    if buttons[row][column]['text'] == "" and check_winner() is False:
        if player == players[0]:
            buttons[row][column]['text'] =player
            if check_winner() is False:
                player = players[1]
                label.config(text=f"{players[1]} turn")
            elif check_winner() is True:
                label.config(text=f"{players[0]} wins")
            elif check_winner() == "Tie":
                label.config(text="Match Tie!!")

        else:
            buttons[row][column]['text'] = player
            if check_winner() is False:
                player = players[0]
                label.config(text=f"{players[0]} turn")
            elif check_winner() is True:
                label.config(text=f"{players[1]} wins")
            elif check_winner() == "Tie":
                label.config(text="Match Tie!!")

def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="lightgreen")
            buttons[row][1].config(bg="lightgreen")
            buttons[row][2].config(bg="lightgreen")
            return True
        
    for column in range(3):
        if buttons[column][0]['text'] == buttons[column][1]['text'] == buttons[column][2]['text'] != "":
            buttons[column][0].config(bg="lightgreen")
            buttons[column][1].config(bg="lightgreen")
            buttons[column][2].config(bg="lightgreen")
            return True
        
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] !="":
        buttons[0][0].config(bg="lightgreen")
        buttons[1][1].config(bg="lightgreen")
        buttons[2][2].config(bg="lightgreen")
        return True
    
    elif buttons[2][0]['text']==buttons[1][1]['text'] == buttons[0][2]['text'] !="":
        buttons[2][0].config(bg="lightgreen")
        buttons[1][1].config(bg="lightgreen")
        buttons[0][2].config(bg="lightgreen")
        return True
    
    elif free_spaces() is False:
        return "Tie"
    else:
        return False

def free_spaces():
    spaces = 9
    for row in range(3):
        for col in range(3):
            if buttons[row][col]['text'] != "":
                spaces -=1

    if spaces == 0:
        return False
    else:
        return True

def reset_game():
    global player
    player = random.choice(players)
    label.config(text=f"{player} turn")
    for row in range(3):
        for col in range(3):
            buttons[row][col]['text'] = ""
            buttons[row][col].config(bg=root.cget('bg'))

root = Tk()
root.title("TIC TAC TOE")
players = ['X', 'O']
player = random.choice(players)

buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

label = Label(root, text=f"{player} turn", font=("courier new",35))
label.pack(side = TOP)

reset_buttom = Button(root, text="Restart Game", font=("courier new",25), command=reset_game)
reset_buttom.pack(side = TOP)

frame = Frame(root)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", width=5, height=2, font=("courier new",35), 
                                      command=lambda row=row, column=column: next_turn(row,column)) 
        buttons[row][column].grid(row=row, column=column)

root.mainloop()
