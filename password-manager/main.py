from tkinter import *
import random
import pyperclip
from tkinter import messagebox

#Display Window
window = Tk()
window.resizable(False, False)
window.geometry("800x700")
window.title("Password Manager")

#Password Image
image = PhotoImage(file="logo.png")
img_display = Label(image=image)
img_display.grid(column=0, row=0)

#Website Label
label1 = Label(text="Website:", font=("Arial", 12, "bold"))
label1.grid(column=0, row=1)

#Website Entry
entry1 = Entry(width=30)
entry1.grid(column=1, row=1)

#Email/Username Label
label2 = Label(text="Email/Username:", font=("Arial", 12, "bold"))
label2.grid(column=0, row=2)

#Email/Username Entry
entry2 = Entry(width=30)
entry2.insert(0, "willashc21@gmail.com")
entry2.grid(column=1, row=2)

#Password Label
label3 = Label(text="Password:", font=("Arial", 12, "bold"))
label3.grid(column=0, row=3)

#Password Entry
entry3 = Entry(width=30)
entry3.config(show="*")
entry3.grid(column=1, row=3)

#Password Characters
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
              't', 'u', 'v', 'w', 'x', 'y', 'z',
              'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
              'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
              '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#Method for Generating Password
def generate_password():
    entry3.delete(0, len(entry3.get()))
    str = ""
    for x in range(0, random.randint(0, 16)):
        character = random.randint(0, len(characters) - 1)
        str += characters[character]
    entry3.insert(0, str)
    pyperclip.copy(entry3.get())


#Saves information to file
def save_info():
    con = messagebox.askokcancel("Confirm?", "This will save the password")
    if con:
        messagebox.showinfo("Saved", "Save Successfully")
        message = messagebox.showinfo("Info", f"{entry1.get()}\n{entry2.get()}\n{entry3.get()}")
        with open("password_info.txt", "a") as f:
            f.write(entry1.get() + " | " + entry2.get() + " | " + entry3.get() + "\n")
            entry1.delete(0, len(entry1.get()))
            entry2.delete(0, len(entry2.get()))
            entry3.delete(0, len(entry3.get()))

#Generate Password Button
gen_button = Button(text="Generate Password", command=generate_password, width=15)
gen_button.grid(column=2, row=3)

#Save Information Button
save_button = Button(text="Add", command=save_info, width=5)
save_button.grid(column=1, row=4)

#Window Display
window.mainloop()