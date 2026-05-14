# Advanced Password Generator

import random
import string
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def generate_password():
    try:
        length = int(length_entry.get())

        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4")
            return

        characters = ""

        if letters_var.get():
            characters += string.ascii_letters

        if numbers_var.get():
            characters += string.digits

        if symbols_var.get():
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Error", "Select at least one character type")
            return

        if exclude_similar_var.get():
            similar = "Il1O0"
            characters = ''.join(ch for ch in characters if ch not in similar)

        exclude_chars = exclude_entry.get()
        characters = ''.join(ch for ch in characters if ch not in exclude_chars)

        if not characters:
            messagebox.showerror("Error", "No characters left after exclusions")
            return

        password = []

        if letters_var.get():
            password.append(random.choice(string.ascii_letters))

        if numbers_var.get():
            password.append(random.choice(string.digits))

        if symbols_var.get():
            password.append(random.choice(string.punctuation))

        while len(password) < length:
            password.append(random.choice(characters))

        # Shuffle password
        random.shuffle(password)

        final_password = ''.join(password)

        # Display password
        password_entry.delete(0, tk.END)
        password_entry.insert(0, final_password)

        # Update strength
        update_strength(final_password)

    except ValueError:
        messagebox.showerror("Error", "Enter a valid number")

# PASSWORD STRENGTH CHECKER

def update_strength(password):

    strength = 0

    if len(password) >= 8:
        strength += 1

    if any(c.islower() for c in password):
        strength += 1

    if any(c.isupper() for c in password):
        strength += 1

    if any(c.isdigit() for c in password):
        strength += 1

    if any(c in string.punctuation for c in password):
        strength += 1

    if strength <= 2:
        strength_label.config(text="Weak", foreground="red")

    elif strength <= 4:
        strength_label.config(text="Medium", foreground="orange")

    else:
        strength_label.config(text="Strong", foreground="green")


# COPY TO CLIPBOARD

def copy_password():
    password = password_entry.get()

    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()

        messagebox.showinfo("Copied", "Password copied to clipboard")
    else:
        messagebox.showwarning("Warning", "No password generated")

# GUI WINDOW

root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("500x500")
root.resizable(False, False)

# TITLE

title_label = tk.Label(
    root,
    text="Advanced Password Generator",
    font=("Arial", 18, "bold")
)
title_label.pack(pady=10)

# PASSWORD LENGTH

length_frame = tk.Frame(root)
length_frame.pack(pady=5)

tk.Label(length_frame, text="Password Length:", font=("Arial", 12)).pack(side=tk.LEFT)

length_entry = tk.Entry(length_frame, width=10, font=("Arial", 12))
length_entry.pack(side=tk.LEFT, padx=10)
length_entry.insert(0, "12")

# CHARACTER OPTIONS

letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)
exclude_similar_var = tk.BooleanVar()

options_frame = tk.Frame(root)
options_frame.pack(pady=10)

tk.Checkbutton(
    options_frame,
    text="Include Letters",
    variable=letters_var,
    font=("Arial", 11)
).pack(anchor="w")

tk.Checkbutton(
    options_frame,
    text="Include Numbers",
    variable=numbers_var,
    font=("Arial", 11)
).pack(anchor="w")

tk.Checkbutton(
    options_frame,
    text="Include Symbols",
    variable=symbols_var,
    font=("Arial", 11)
).pack(anchor="w")

tk.Checkbutton(
    options_frame,
    text="Exclude Similar Characters (I, l, 1, O, 0)",
    variable=exclude_similar_var,
    font=("Arial", 11)
).pack(anchor="w")

# ----------------------------
# EXCLUDE CUSTOM CHARACTERS
# ----------------------------
exclude_frame = tk.Frame(root)
exclude_frame.pack(pady=10)

tk.Label(
    exclude_frame,
    text="Exclude Characters:",
    font=("Arial", 12)
).pack(side=tk.LEFT)

exclude_entry = tk.Entry(exclude_frame, width=20, font=("Arial", 12))
exclude_entry.pack(side=tk.LEFT, padx=10)

# GENERATE BUTTON

generate_button = tk.Button(
    root,
    text="Generate Password",
    font=("Arial", 12, "bold"),
    bg="lightblue",
    command=generate_password
)
generate_button.pack(pady=15)

# PASSWORD OUTPUT

password_entry = tk.Entry(
    root,
    width=35,
    font=("Arial", 14),
    justify="center"
)
password_entry.pack(pady=10)

# COPY BUTTON

copy_button = tk.Button(
    root,
    text="Copy to Clipboard",
    font=("Arial", 12),
    bg="lightgreen",
    command=copy_password
)
copy_button.pack(pady=10)

# PASSWORD STRENGTH

strength_text = tk.Label(
    root,
    text="Password Strength:",
    font=("Arial", 12, "bold")
)
strength_text.pack()

strength_label = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold")
)
strength_label.pack(pady=5)

root.mainloop()
