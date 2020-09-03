import tkinter
from random import choice


window = tkinter.Tk()
window.title("Rock, paper, scissors")

choices = ["Rock", "Paper", "Scissors"]
player_score = tkinter.IntVar()
computer_score = tkinter.IntVar()
result = tkinter.StringVar()


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




#---------------Main---------------


window.mainloop()
