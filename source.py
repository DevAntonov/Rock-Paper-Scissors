import tkinter
from tkinter import *
from random import choice
from PIL import Image, ImageTk

window = tkinter.Tk()
window.geometry("880x660")
window.title("Rock, paper, scissors")
window.config(bg="gray")

choices = ["Rock", "Paper", "Scissors"]
player_score = IntVar()
computer_score = IntVar()
result = StringVar()
player_last_pick = StringVar()
computer_last_pick = StringVar()



#_______________Images_______________

rock_image = ImageTk.PhotoImage(Image.open("rock_img.jpg"))
paper_image = ImageTk.PhotoImage(Image.open("paper_img.jpg"))
scissors_image = ImageTk.PhotoImage(Image.open("scissors_img.jpg"))


#---------------Game_functions---------------

def if_rock_is_picked():
    player_last_pick.set("Rock")
    computer_pick = choice(choices)
    computer_last_pick.set(computer_pick)

    if computer_pick is "Rock":
        result.set("It's draw!")

    elif computer_pick is "Paper":
        result.set("You win!")
        player_score.set(player_score.get() + 1)

    elif computer_pick is "Scissors":
        result.set("You lose!")
        computer_score.set(computer_score.get() + 1)

    if player_score.get() > computer_score.get():
        player_score_entry.config(bg="green")
        computer_score_entry.config(bg="red")
    elif player_score.get() < computer_score.get():
        player_score_entry.config(bg="red")
        computer_score_entry.config(bg="green")
    else:
        player_score_entry.config(bg="yellow")
        computer_score_entry.config(bg="yellow")


def if_paper_is_picked():
    player_last_pick.set("Rock")
    computer_pick = choice(choices)
    computer_last_pick.set(computer_pick)

    if computer_pick is "Paper":
        result.set("You lose!")
        computer_score.set(computer_score.get() + 1)

    elif computer_pick is "Paper":
        result.set("It's draw!")

    elif computer_pick is "Scissors":
        result.set("You win!")
        player_score.set(player_score.get() + 1)

    if player_score.get() > computer_score.get():
        player_score_entry.config(bg="green")
        computer_score_entry.config(bg="red")
    elif player_score.get() < computer_score.get():
        player_score_entry.config(bg="red")
        computer_score_entry.config(bg="green")
    else:
        player_score_entry.config(bg="yellow")
        computer_score_entry.config(bg="yellow")

def if_scissors_is_picked():
    player_last_pick.set("Scissors")
    computer_pick = choice(choices)
    computer_last_pick.set(computer_pick)

    if computer_pick is "Rock":
        result.set("You win!")
        player_score.set(player_score.get() + 1)

    elif computer_pick is "Paper":
        result.set("You lose!")
        computer_score.set(computer_score.get() + 1)

    elif computer_pick is "Scissors":
        result.set("It's draw!")

    if player_score.get() > computer_score.get():
        player_score_entry.config(bg="green")
        computer_score_entry.config(bg="red")
    elif player_score.get() < computer_score.get():
        player_score_entry.config(bg="red")
        computer_score_entry.config(bg="green")
    else:
        player_score_entry.config(bg="yellow")
        computer_score_entry.config(bg="yellow")

def reset():
    player_score.set(0)
    computer_score.set(0)
    result.set("")
    player_last_pick.set("")
    computer_last_pick.set("")
    player_score_entry.config(bg="yellow")
    computer_score_entry.config(bg="yellow")

def exit_game():
    window.destroy()

#---------------GUI---------------

message = Label(window, text="Pick rock, paper or scissors", font=("Arial", 20), relief=GROOVE)
message.place(relx=0.5, rely=0.05, anchor=CENTER)

rock_button = Button(window, width=230, height=230, image=rock_image, command=if_rock_is_picked, relief=GROOVE)
rock_button.place(relx=0.2, rely=0.35, anchor=CENTER)

paper_button = Button(window, width=230, height=230, image=paper_image, command=if_paper_is_picked, relief=GROOVE)
paper_button.place(relx=0.5, rely=0.35, anchor=CENTER)

scissors_button = Button(window, width=230, height=230, image=scissors_image, command=if_scissors_is_picked, relief=GROOVE)
scissors_button.place(relx=0.8, rely=0.35, anchor=CENTER)

win_or_lose_entry = Entry(window, textvariable=result, width=30, font=("Arial", 20), relief=GROOVE)
win_or_lose_entry.place(relx=0.5, rely=0.6, anchor=CENTER)

player_score_entry = Entry(window, textvariable=player_score, width=3, bg="yellow", font=("Arial", 20), relief=GROOVE)
player_score_entry.place(relx=0.2, rely=0.1, anchor=CENTER)

computer_score_entry = Entry(window, textvariable=computer_score, width=3, bg="yellow", font=("Arial", 20), relief=GROOVE)
computer_score_entry.place(relx=0.8, rely=0.1, anchor=CENTER)


player_last_pick_entry = Entry(window, textvariable=player_last_pick, width=10, font=("Arial", 20), relief=GROOVE)
player_last_pick_entry.place(relx=0.55, rely=0.7, anchor=CENTER)

computer_last_pick_entry = Entry(window, textvariable=computer_last_pick, width=10, font=("Arial", 20), relief=GROOVE)
computer_last_pick_entry.place(relx=0.55, rely=0.8, anchor=CENTER)

plr_txt = Label(window, text="You: ", font=("Arial", 20), relief=GROOVE)
plr_txt.place(relx=0.404, rely=0.7, anchor=CENTER)

com_txt = Label(window, text="Com: ", font=("Arial", 20), relief=GROOVE)
com_txt.place(relx=0.4, rely=0.8, anchor=CENTER)

reset_button = Button(window, text="Reset", width=10, height=2, command=reset, bg="yellow", activebackground="red", relief=GROOVE)
reset_button.place(relx=0.45, rely=0.9, anchor=CENTER)

exit_button = Button(window, text="Exit", width=10, height=2, command=exit_game, bg="red", activebackground="red", relief=GROOVE)
exit_button.place(relx=0.55, rely=0.9, anchor=CENTER)


#---------------Main---------------



window.mainloop()
