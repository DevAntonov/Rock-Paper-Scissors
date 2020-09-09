import tkinter
from tkinter import *
from random import choice
from PIL import Image, ImageTk

window = tkinter.Tk()
window.geometry("880x660")
window.title("Rock, paper, scissors")

choices = ["Rock", "Paper", "Scissors"]
player_score = IntVar()
computer_score = IntVar()
result = StringVar()
player_last_pick = StringVar()
computer_last_pick = StringVar()

score_bg_color_player = StringVar()
score_bg_color_player.set("yellow")
score_bg_color_computer = StringVar()
score_bg_color_computer.set("yellow")


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
        score_bg_color_player.set("green")
        score_bg_color_computer.set("red")
    elif player_score.get() < computer_score.get():
        score_bg_color_player.set("red")
        score_bg_color_computer.set("green")
    else:
        score_bg_color_player.set("yellow")
        score_bg_color_computer.set("yellow")


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
        score_bg_color_player.set("green")
        score_bg_color_computer.set("red")
    elif player_score.get() < computer_score.get():
        score_bg_color_player.set("red")
        score_bg_color_computer.set("green")
    else:
        score_bg_color_player.set("yellow")
        score_bg_color_computer.set("yellow")

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
        score_bg_color_player.set("green")
        score_bg_color_computer.set("red")
    elif player_score.get() < computer_score.get():
        score_bg_color_player.set("red")
        score_bg_color_computer.set("green")
    else:
        score_bg_color_player.set("yellow")
        score_bg_color_computer.set("yellow")

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

player_score_entry = Entry(window, textvariable=player_score, width=3, bg=score_bg_color_player.get(), font=("Arial", 20), relief=GROOVE)
player_score_entry.place(relx=0.2, rely=0.1, anchor=CENTER)

computer_score_entry = Entry(window, textvariable=computer_score, width=3, bg=score_bg_color_computer.get(), font=("Arial", 20), relief=GROOVE)
computer_score_entry.place(relx=0.8, rely=0.1, anchor=CENTER)

player_last_pick_entry = Entry(window, textvariable=player_last_pick, width=10, font=("Arial", 20), relief=GROOVE)
player_last_pick_entry.place(relx=0.35, rely=0.8, anchor=CENTER)

computer_last_pick_entry = Entry(window, textvariable=computer_last_pick, width=10, font=("Arial", 20), relief=GROOVE)
computer_last_pick_entry.place(relx=0.65, rely=0.8, anchor=CENTER)

exit_button = Button(window, text="Exit", width=10, height=2, command=exit_game, bg="red", activebackground="red", relief=GROOVE)
exit_button.place(relx=0.5, rely=0.9, anchor=CENTER)


#---------------Main---------------


window.mainloop()
