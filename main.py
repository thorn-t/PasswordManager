from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generatePassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    passTextbox.insert(0, password)


# SAVE PASSWORD
def savePassword():
    website = websiteTextbox.get()
    user = userTextbox.get()
    pw = passTextbox.get()
    newData = {
        website: {
            "email": user,
            "password": pw,
        }
    }

    if len(website) <= 0 or len(pw) <= 0:
        messagebox.showinfo(title="Invalid input", message="Please fill in any empty fields.")

    else:
        try:
            with open("text.json", mode="r") as file:
                # reading old data
                data = json.load(file)
                # updating old data with new data
                data.update(newData)
        except FileNotFoundError:
            with open("text.json", mode="w") as file:
                json.dump(newData, file, indent=4)
        else:
            with open("text.json", mode="w") as file:
                # save the data
                json.dump(data, file, indent=4)
        finally:
            websiteTextbox.delete(0, END)
            passTextbox.delete(0, END)


# Search
def search():
    website = websiteTextbox.get()
    try:
        with open("text.json", mode="r") as file:
            # reading old data
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title=website, message=f"No data file found")
    else:
        if website in data:
            curPass = data[website]
            messagebox.showinfo(title=website, message=f"Email: {curPass['email']}\n"
                                                       f"Password: {curPass['password']}")
        else:
            messagebox.showinfo(title=website, message=f"no deatils about {website}")
    finally:
        websiteTextbox.delete(0, END)


# UI Setup
window = Tk()
window.title("Password manager")
window.config(padx=10, pady=10)

# Website label
websiteLabel = Label(text="Website:")
websiteLabel.grid(column=0, row=1)

# Website textbox
websiteTextbox = Entry(width=35)
websiteTextbox.focus()
websiteTextbox.grid(column=1, row=1, columnspan=2, sticky=EW)

# User label
userLabel = Label(text="Email/Username:")
userLabel.grid(column=0, row=2)

# User textbox
userTextbox = Entry(width=35)
userTextbox.insert(0, "test@gmail.com")
userTextbox.grid(column=1, row=2, columnspan=2, sticky=EW)

# Pass label
passLabel = Label(text="Password:")
passLabel.grid(column=0, row=3)

# Pass textbox
passTextbox = Entry(width=21)
passTextbox.grid(column=1, row=3, sticky=EW)

# Pass button
passButton = Button(text="Generate Password", command=generatePassword)
passButton.grid(column=2, row=3, sticky=EW)

# Add button
addButton = Button(text="Add", width=36, command=savePassword)
addButton.grid(column=1, row=4, columnspan=2, sticky=EW)

# Search button
passButton = Button(text="Search", command=search)
passButton.grid(column=2, row=1, sticky=EW)

window.mainloop()
