from tkinter import *
import customtkinter
from PIL import Image, ImageTk
import random

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("Magicball")
root.geometry("500x500")

def shake():
    answers = {
        "it i s certain": "green",
        "It is decidely so": "green",
        "Without a doubt": "green",
        "Yes definetely": "green",
        "You may rely on it": "green",
        "As I see it, yes": "green",
        "Most likely": "green",
        "Outlook good": "green",
        "Yes": "green",
        "Signs point to yes": "green",

        "Reply hazy, try again": "yellow",
        "Ask again later": "yellow",
        "Better not tell you now": "yellow",
        "Cannot predict now": "yellow",
        "concetrate and ask again": "yellow",

        "Don't count on it": "red",
        "My reply is no": "red",
        "My sources say no": "red",
        "Outlook not so good": "red",
        "Very doubtful": "red"
    }

    #convert dictionary to list
    answer_list = list(answers.items())
    random.shuffle(answer_list)
    results.config(text=answer_list[0][0], fg=answer_list[0][1])

ball = ImageTk.PhotoImage(Image.open("1vecteezy_billiard-ball.png"))
ball_img = Label(root, image=ball, bd=0)
ball_img.pack(pady=20)

results = Label(root, text="", font=("verdana", 28), bg="#1a1a1a")
results.pack(pady=20)

mt_btn = customtkinter.CTkButton(master=root, text="Shake 8-ball", width=190, height=40, compound="top",
                                 command=shake)
mt_btn.pack(pady=20)

root.mainloop()
