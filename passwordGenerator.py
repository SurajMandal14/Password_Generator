import tkinter as tk
import string
import random


def generate_password():
    password_length = int(entry_length.get())
    complexity = var.get()

    if complexity == 1:
        characters = string.ascii_letters + string.digits
    elif complexity == 2:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        characters = string.ascii_letters + string.digits + \
            string.punctuation + string.ascii_lowercase

    password = ''.join(random.choice(characters)
                       for i in range(password_length))
    label_password.config(text=f"Generated Password: {password}")


root = tk.Tk()
root.title("Password Generator")

frame = tk.Frame(root)
frame.pack(padx=100, pady=100)

label_length = tk.Label(
    frame, text="Enter Password Length:", font=("Arial", 12))
label_length.grid(row=0, column=0, pady=5)

entry_length = tk.Entry(frame, font=("Arial", 12))
entry_length.grid(row=0, column=1, pady=5)

label_complexity = tk.Label(
    frame, text="Select Complexity Level:", font=("Arial", 12))
label_complexity.grid(row=1, column=0, pady=5)

var = tk.IntVar()
var.set(1)

radio_simple = tk.Radiobutton(
    frame, text="Simple", variable=var, value=1, font=("Arial", 12))
radio_simple.grid(row=1, column=1, pady=5)

radio_medium = tk.Radiobutton(
    frame, text="Medium", variable=var, value=2, font=("Arial", 12))
radio_medium.grid(row=1, column=2, pady=5)

radio_strong = tk.Radiobutton(
    frame, text="Strong", variable=var, value=3, font=("Arial", 12))
radio_strong.grid(row=1, column=3, pady=5)

button_generate = tk.Button(
    frame, text="Generate Password", command=generate_password, font=("Arial", 12))
button_generate.grid(row=2, columnspan=4, pady=10)

label_password = tk.Label(
    frame, text="Generated Password: ", font=("Arial", 14))
label_password.grid(row=3, columnspan=4, pady=10)

root.mainloop()
