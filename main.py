import random
import string
import customtkinter as ctk
from customtkinter import CTk, CTkLabel, CTkButton, CTkComboBox
from ttkthemes import ThemedTk
import tkinter as ttk

# function to generate password
def generate_password(*args):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for i in range(var.get()))
    output.config(text = password)
    output.config(text = password, font = ("Ubuntu", 20), justify = 'center')

# function to copy the password to clipboard
def copy_to_clipboard():
    app.clipboard_clear()
    app.clipboard_append(output['text']) # Use cget() to get the text

# create themed customtkinter window
app = CTk()
app.title("Password Generator")
app.geometry("960x540")

# variable to hold the number of characters in the password
var = ctk.IntVar()
var.set(8)

# create a dropdown menu for the number of characters
dropdown = ttk.Combobox(app, textvariable= var, values= [8,9,10,11,12,13,14,15,16,17,18,19,20])
dropdown.pack(pady = 5)

# create 'generate' button
generate_button = ttk.Button(app, text="Generate", command= generate_password)
generate_button.pack(pady = 5)

# create 'copy' button
copy_button = ttk.Button(app, text="Copy", command= copy_to_clipboard)
copy_button.pack(pady = 5)

# create output field
output = ttk.Label(app)
output.pack(pady = 20)

# run the main loop
app.mainloop()