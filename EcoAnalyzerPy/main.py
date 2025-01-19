# bin and main.py will be for setting up the environment and starting the program

'''This file offers functions to answer the research questions discussed in
description.txt.'''
import sys
import os
from tkinter import *
from controller import rq_1_land as rq_1
from controller import rq_3_co2 as rq_3
from controller import rq_4_species as rq_4
from controller import rq_5_land_co2 as rq_5
from controller import rq_6_land_co2 as rq_6
from controller import rq_7_species_controller as rq_7
from controller import rq_8_species_controller as rq_8
from controller import rq_9_species_controller as rq_9
from controller import rq_10_species_controller as rq_10

def run_controller():
    window = Tk()
    window.title("EcoAnalzyerPy")

    # we adjust the size of the window
    window.geometry("400x300")

    # we get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # we calculate the position to center the window
    x = int((screen_width - 400) / 2)
    y = int((screen_height - 300) / 2)

    # i set the window position now
    window.geometry(f"+{x}+{y}")

    label = Label(window, text="Welcome to EcoAnalzyerPy!")
    label.pack()

    button1 = Button(window, text="Research Question 1", command=rq_1.research_question_one)
    button1.pack()


    button3 = Button(window, text="Research Question 3", command=rq_3.research_question_three)
    button3.pack()

    button4 = Button(window, text="Research Question 4", command=rq_4.research_question_four)
    button4.pack()

    button5 = Button(window, text="Research Question 5", command=rq_5.research_question_five)
    button5.pack()

    button6 = Button(window, text="Research Question 6", command=rq_6.research_question_six)
    button6.pack()

    button7 = Button(window, text="Research Question 7", command=rq_7.research_question_seven)
    button7.pack()

    button8 = Button(window, text="Research Question 8", command=rq_8.research_question_eight)
    button8.pack()

    button9 = Button(window, text="Research Question 9", command=rq_9.research_question_nine)
    button9.pack()

    button10 = Button(window, text="Research Question 10", command=rq_10.research_question_ten)
    button10.pack()

    exit_button = Button(window, text="Exit", command=window.quit)
    exit_button.pack()

    window.mainloop()

if __name__ == '__main__':
    run_controller()