from tkinter import *
import pandas
import random

window = Tk()
window.title("Flash Cards")
window.minsize(width=1000, height=850)
window.resizable(False, False)
canvas = Canvas(bg="#00F5FF", width=1000, height=850)

data = pandas.read_csv("french_words.csv")
french = data["French"].tolist()
french_len = len(french)
num = random.randint(0, 101)
french_word = french[num - 1]
my_image1 = PhotoImage(file="card_front.png")
img_display = canvas.create_image(505, 300, anchor="center", image=my_image1)
canvas.delete('fr')
canvas.delete('al')


my_image = PhotoImage(file="card_back.png")
def eng_word(num):
    canvas.delete('fr')
    canvas.delete('al')
    english = data["English"].tolist()
    english_word = english[num]
    print(num)
    canvas.itemconfig(img_display, image=my_image)
    title_english_display = canvas.create_text(500, 250, fill="black", text="English Word", font=("Arial", 32, "italic"), tags="al")
    english_word_display = canvas.create_text(500, 350, fill="black", text=english_word, font=("Arial", 32, "bold"),
                                             tags="fr")
    canvas.pack()

def generate_word():
    canvas.delete('fr')
    canvas.delete('al')
    num = random.randint(0, 101)
    french_word = french[num - 1]
    print(num - 1)
    canvas.itemconfig(img_display, image=my_image1)
    title_french_display = canvas.create_text(500, 250, fill="black", text="French Word", font=("Arial", 32, "italic"), tags="al")
    french_word_display = canvas.create_text(500, 350, fill="black", text=french_word, font=("Arial", 32, "bold"), tags="fr")
    window.after(3000, eng_word, num - 1)

generate_word()

my_image2 = PhotoImage(file="right.png")
right_button = Button(command=generate_word, image=my_image2)
right_button.place(x=705, y=660)

my_image3 = PhotoImage(file="wrong.png")
wrong_button = Button(command=generate_word, image=my_image3)
wrong_button.place(x=255, y=660)



title_french_display = canvas.create_text(500, 250, fill="black", text="French Word", font=("Arial", 32, "italic"), tags="al")
french_word_display = canvas.create_text(-500, 350, fill="black", text=french_word, font=("Arial", 32, "bold"), tags="fr")
canvas.pack()
window.mainloop()