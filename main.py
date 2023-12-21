import random
import string
import customtkinter as ctk
from customtkinter import CTk, CTkLabel, CTkButton, CTkComboBox
from ttkthemes import ThemedTk

# function to generate password
def generate_password(*args):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(var.get()))
    output.configure_text(password, font=("Ubuntu", 20), justify='center')  # Use configure_text() instead of direct assignment

# function to copy the password to clipboard
def copy_to_clipboard():
    app.clipboard_clear()
    app.clipboard_append(output.cget("text"))  # Use cget() to get the text

# create themed customtkinter window
app = CTk()
app.title("Password Generator")
app.geometry("960x540")

# variable to hold the number of characters in the password
var = ctk.IntVar()
var.set(8)

# create a dropdown menu for the number of characters
values = [str(i) for i in range(8, 21)]  # Convert integers to strings
dropdown = CTkComboBox(app, values=values)
dropdown.pack(pady=5)
dropdown.bind("<<ComboboxSelected>>", generate_password)  # Bind the event to generate_password

# create 'generate' button
generate_button = CTkButton(app, text="Generate", command=generate_password)
generate_button.pack(pady=5)

# create 'copy' button
copy_button = CTkButton(app, text="Copy", command=copy_to_clipboard)
copy_button.pack(pady=5)



# run the main loop
app.mainloop()
