# Import Required Library
import tkinter as tk
import random

# Create Object
root = tk.Tk()

# Set geometry
root.geometry("600x300")

# Set title
root.title("Rock Paper Scissor Game")

# Computer Value
computer_value = {
    "0":"Rock",
    "1":"Paper",
    "2":"Scissor"
}

# Reset The Game
def reset_game():
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"
    l1.config(text = "Player             ")
    l3.config(text = "Computer")
    l4.config(text = "")

# Disable the Button
def button_disable():
    b1["state"] = "disable"
    b2["state"] = "disable"
    b3["state"] = "disable"

# If player selected rock
def isrock():
    com_val = computer_value[str(random.randint(0,2))]
    if com_val == "Rock":
        match_result = "Match Draw"
    elif com_val=="Scissor":
        match_result = "Player Win"
    else:
        match_result = "Computer Win"
    l4.config(text = match_result)
    l1.config(text = "Rock       ")
    l3.config(text = com_val)
    button_disable()

# If player selected paper
def ispaper():
    com_val = computer_value[str(random.randint(0, 2))]
    if com_val == "Paper":
        match_result = "Match Draw"
    elif com_val=="Scissor":
        match_result = "Computer Win"
    else:
        match_result = "Player Win"
    l4.config(text = match_result)
    l1.config(text = "Paper      ")
    l3.config(text = com_val)
    button_disable()

# If player selected scissors
def isscissor():
    com_val = computer_value[str(random.randint(0,2))]
    if com_val == "Rock":
        match_result = "Computer Win"
    elif com_val == "Scissor":
        match_result = "Match Draw"
    else:
        match_result = "Player Win"
    l4.config(text = match_result)
    l1.config(text = "Scissor        ")
    l3.config(text = com_val)
    button_disable()

# Add Labels, Frames and Button
tk.Label(root,
    text = "Rock Paper Scissor",
    font = "normal 20 bold",
    fg = "blue").pack(pady = 20)

frame = tk.Frame(root)
frame.pack()

l1 = tk.Label(frame,
        text = "Player            ",
        font = 10)

l2 = tk.Label(frame,
        text = "VS          ",
        font = "normal 10 bold")

l3 = tk.Label(frame, text = "Computer", font = 10)

l1.pack(side = tk.LEFT)
l2.pack(side = tk.LEFT)
l3.pack()

l4 = tk.Label(root,
        text = "",
        font = "normal 20 bold",
        bg = "white",
        width = 15 ,
        borderwidth = 2,
        relief = "solid")
l4.pack(pady = 20)

frame1 = tk.Frame(root)
frame1.pack()

b1 = tk.Button(frame1, text = "Rock",
            font = 10, width = 7,
            command = isrock)

b2 = tk.Button(frame1, text = "Paper ",
            font = 10, width = 7,
            command = ispaper)

b3 = tk.Button(frame1, text = "Scissor",
            font = 10, width = 7,
            command = isscissor)

b1.pack(side = tk.LEFT, padx = 10)
b2.pack(side = tk.LEFT,padx = 10)
b3.pack(padx = 10)

tk.Button(root, text = "Reset Game",
    font = 10, fg = "red",
    bg = "black", command = reset_game).pack(pady = 20)

# Excecute Tkinter
root.mainloop()
