from tkinter import *
from tkinter import messagebox


# ---------------- RESET FUNCTION ---------------- #

def reset_entry():
    age_tf.delete(0, END)
    height_tf.delete(0, END)
    weight_tf.delete(0, END)
    var.set(0)


# ---------------- BMI CALCULATION ---------------- #

def calculate_bmi():

    try:
        age = int(age_tf.get())
        height = float(height_tf.get())
        weight = float(weight_tf.get())

        # Validation
        if age < 2 or age > 120:
            messagebox.showerror("Invalid Age", "Age must be between 2 and 120")
            return

        if height <= 0 or weight <= 0:
            messagebox.showerror("Invalid Input", "Height and Weight must be positive")
            return

        if var.get() == 0:
            messagebox.showerror("Gender Error", "Please select gender")
            return

        # Convert cm to meter
        height_m = height / 100

        # BMI Formula
        bmi = weight / (height_m ** 2)
        bmi = round(bmi, 1)

        bmi_index(bmi)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")


# ---------------- BMI CATEGORY ---------------- #

def bmi_index(bmi):

    if bmi < 18.5:
        category = "Underweight"

    elif 18.5 <= bmi <= 24.9:
        category = "Normal Weight"

    elif 25 <= bmi <= 29.9:
        category = "Overweight"

    else:
        category = "Obesity"

    messagebox.showinfo(
        "BMI Result",
        f"Your BMI = {bmi}\nCategory = {category}"
    )


# ---------------- MAIN WINDOW ---------------- #

ws = Tk()
ws.title("BMI Calculator")
ws.geometry("420x320")
ws.config(bg="#686e70")


# Gender Variable
var = IntVar()


# ---------------- FRAME ---------------- #

frame = Frame(
    ws,
    padx=15,
    pady=15,
    bg="white"
)

frame.pack(expand=True)


# ---------------- AGE ---------------- #

age_lb = Label(
    frame,
    text="Enter Age (2 - 120)",
    bg="white"
)

age_lb.grid(row=0, column=0, sticky=W)

age_tf = Entry(frame)
age_tf.grid(row=0, column=1, pady=5)


# ---------------- GENDER ---------------- #

gen_lb = Label(
    frame,
    text="Select Gender",
    bg="white"
)

gen_lb.grid(row=1, column=0, sticky=W)

frame2 = Frame(frame, bg="white")
frame2.grid(row=1, column=1, pady=5)

male_rb = Radiobutton(
    frame2,
    text="Male",
    variable=var,
    value=1,
    bg="white"
)

male_rb.pack(side=LEFT)

female_rb = Radiobutton(
    frame2,
    text="Female",
    variable=var,
    value=2,
    bg="white"
)

female_rb.pack(side=LEFT)


# ---------------- HEIGHT ---------------- #

height_lb = Label(
    frame,
    text="Enter Height (cm)",
    bg="white"
)

height_lb.grid(row=2, column=0, sticky=W)

height_tf = Entry(frame)
height_tf.grid(row=2, column=1, pady=5)


# ---------------- WEIGHT ---------------- #

weight_lb = Label(
    frame,
    text="Enter Weight (kg)",
    bg="white"
)

weight_lb.grid(row=3, column=0, sticky=W)

weight_tf = Entry(frame)
weight_tf.grid(row=3, column=1, pady=5)


# ---------------- BUTTONS ---------------- #

frame3 = Frame(frame, bg="white")
frame3.grid(row=4, columnspan=2, pady=15)

cal_btn = Button(
    frame3,
    text="Calculate BMI",
    command=calculate_bmi,
    width=15,
    bg="lightgreen"
)

cal_btn.pack(side=LEFT, padx=5)

reset_btn = Button(
    frame3,
    text="Reset",
    command=reset_entry,
    width=10,
    bg="lightblue"
)

reset_btn.pack(side=LEFT, padx=5)

exit_btn = Button(
    frame3,
    text="Exit",
    command=ws.destroy,
    width=10,
    bg="tomato"
)

exit_btn.pack(side=LEFT, padx=5)


# ---------------- RUN APP ---------------- #

ws.mainloop()