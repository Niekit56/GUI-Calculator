import tkinter as tk
from tkinter import messagebox

# Create the main window
win = tk.Tk()
win.geometry(f"240x270+100+200")
win["bg"] = "black"  # 33ffe6
win.title("Calculator")
win.resizable(width=False, height=False)

# Function to handle key press event
def press_key(event):
    print(repr(event.char))
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in "+-/*":
        add_operation(event.char)
    elif event.char == "\r":
        calculate()

# Bind key press event to the main window
win.bind("<Key>", press_key)

# Function to add a digit to the calculator display
def add_digit(digit):
    value = calc.get()
    if value[0] == "0" and len(value) == 1:
        value = value[1:]
    calc.delete(0, tk.END)
    calc.insert(0, value + digit)

# Function to add an operation to the calculator display
def add_operation(operation):
    value = calc.get()
    if value[-1] in "-+/*":
        value = value[:-1]
    elif "+" in value or "-" in value or "*" in value or "/" in value:
        calculate()
        value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, value + operation)

# Function to perform calculation
def calculate():
    value = calc.get()
    if value[-1] in "-+/*":
        value = value + value[:-1]
    calc.delete(0, tk.END)
    try:
        calc.insert(0, eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo('Warning', "You only need numbers!!! You have entered other characters")
        calc.insert(0, 0)
    except ZeroDivisionError:
        messagebox.showinfo("Attention", "You can't divide by zero!")
        calc.insert(0, 0)

# Function to clear the calculator display
def clear():
    calc.delete(0, tk.END)
    calc.insert(0, 0)

# Function to create an operation button
def make_digit_button(digit):
    return tk.Button(text=digit, bd=5, font=("arial", 13), command=lambda: add_digit(digit))

# Function to create a digit button
def make_operation_button(operation):
    return tk.Button(text=operation, bd=5, font=("arial", 13), fg="red",
                     command=lambda: add_operation(operation))

# Function to create an operation button
def make_culc_button(operation):
    return tk.Button(text=operation, bd=5, font=("arial", 13), fg="red",
                     command=calculate)

# Function to create a calculate button
def make_clear_button(operation):
    return tk.Button(text=operation, bd=5, font=("arial", 13), fg="red",
                     command=clear)

# Create an entry widget for the calculator display
calc = tk.Entry(win, justify=tk.RIGHT, font=("arial", 15,), width=15)
calc.insert(0, "0")
calc.grid(row=0, column=0, columnspan=4, stick="we", padx=5)  # columnspan - joins columns(3)

# Create digit buttons and place them on the grid
make_digit_button("1").grid(row=1, column=0, stick="wens", padx=5, pady=5)
make_digit_button("2").grid(row=1, column=1, stick="wens", padx=5, pady=5)
make_digit_button("3").grid(row=1, column=2, stick="wens", padx=5, pady=5)
make_digit_button("4").grid(row=2, column=0, stick="wens", padx=5, pady=5)
make_digit_button("5").grid(row=2, column=1, stick="wens", padx=5, pady=5)
make_digit_button("6").grid(row=2, column=2, stick="wens", padx=5, pady=5)
make_digit_button("7").grid(row=3, column=0, stick="wens", padx=5, pady=5)
make_digit_button("8").grid(row=3, column=1, stick="wens", padx=5, pady=5)
make_digit_button("9").grid(row=3, column=2, stick="wens", padx=5, pady=5)
make_digit_button("0").grid(row=4, column=0, stick="wens", padx=5, pady=5)

# Create operation buttons and place them on the grid
make_operation_button("+").grid(row=1, column=3, stick="wens", padx=5, pady=5)
make_operation_button("-").grid(row=2, column=3, stick="wens", padx=5, pady=5)
make_operation_button("/").grid(row=3, column=3, stick="wens", padx=5, pady=5)
make_operation_button("*").grid(row=4, column=3, stick="wens", padx=5, pady=5)

# Create calculate and clear buttons and place them on the grid
make_culc_button("=").grid(row=4, column=2, stick="wens", padx=5, pady=5)
make_clear_button("C").grid(row=4, column=1, stick="wens", padx=5, pady=5)

# Configure column sizes
for i in range(4):
    win.grid_columnconfigure(i, minsize=60)

# Configure row sizes
for i in range(1, 5):
    win.grid_rowconfigure(i, minsize=60)

# Start the GUI event loop
win.mainloop()