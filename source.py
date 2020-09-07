import tkinter
from tkinter import *
from random import choice
from PIL import Image, ImageTk

window = tkinter.Tk()
window.geometry("880x660")
window.title("Rock, paper, scissors")

choices = ["Rock", "Paper", "Scissors"]
player_score = tkinter.IntVar()
computer_score = tkinter.IntVar()
result = tkinter.StringVar()


#_______________Images_______________

rock_image = ImageTk.PhotoImage(Image.open("rock_img.jpg"))
paper_image = ImageTk.PhotoImage(Image.open("paper_img.jpg"))
scissors_image = ImageTk.PhotoImage(Image.open("scissors_img.jpg"))


#---------------Game_functions---------------

def if_rock_is_picked():
    computer_pick = choice(choices)

    if computer_pick is "Rock":
        result.set("It's draw!")

    elif computer_pick is "Paper":
        result.set("You win!")
        player_score.set(player_score.get() + 1)

    elif computer_pick is "Scissors":
        result.set("You lose!")
        computer_score.set(computer_score.get() + 1)


def if_paper_is_picked():
    computer_pick = choice(choices)

    if computer_pick is "Rock":
        result.set("You lose!")
        computer_score.set(computer_score.get() + 1)

    elif computer_pick is "Paper":
        result.set("It's draw!")

    elif computer_pick is "Scissors":
        result.set("You win!")
        player_score.set(player_score.get() + 1)


def if_scissors_is_picked():
    computer_pick = choice(choices)

    if computer_pick is "Rock":
        result.set("You win!")
        player_score.set(player_score.get() + 1)

    elif computer_pick is "Paper":
        result.set("You lose!")
        computer_score.set(computer_score.get() + 1)

    elif computer_pick is "Scissors":
        result.set("It's draw!")



#---------------GUI---------------

message = Label(window, text="Pick rock, paper or scissors", font=("Arial", 20), relief=GROOVE)
message.place(relx=0.5, rely=0.1, anchor=CENTER)

rock_button = Button(window, width=230, height=230, image=rock_image, command=if_rock_is_picked(), relief=GROOVE)
rock_button.place(relx=0.2, rely=0.35, anchor=CENTER)

paper_button = Button(window, width=230, height=230, image=paper_image, command=if_paper_is_picked(), relief=GROOVE)
paper_button.place(relx=0.5, rely=0.35, anchor=CENTER)

scissors_button = Button(window, width=230, height=230, image=scissors_image, command=if_scissors_is_picked(), relief=GROOVE)
scissors_button.place(relx=0.8, rely=0.35, anchor=CENTER)



#---------------Main---------------


window.mainloop()
