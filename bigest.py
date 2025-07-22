# Python Scientific Calculator using tkinter
# This script creates a GUI calculator with trigonometric functions.

import tkinter as tk
from tkinter import messagebox
import math

# --- Function Definitions ---

def button_click(item):
    """
    This function is called when a number or operator button is pressed.
    It appends the pressed item to the expression in the entry field.
    """
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def button_clear():
    """
    This function is called when the 'C' button is pressed.
    It clears the expression and the entry field.
    """
    global expression
    expression = ""
    input_text.set("")

def button_backspace():
    """
    This function is called when the '⌫' button is pressed.
    It removes the last character from the expression.
    """
    global expression
    expression = expression[:-1]
    input_text.set(expression)

def button_equal():
    """
    This function is called when the '=' button is pressed.
    It evaluates the expression in the entry field and displays the result.
    It includes error handling for invalid expressions (e.g., division by zero, syntax errors).
    Note: The 'math' module is imported, so eval() can handle math functions.
    """
    global expression
    try:
        # The eval() function evaluates the passed string as a Python expression.
        # For example, eval('math.sin(math.pi/2)') will return 1.0.
        result = str(eval(expression))
        input_text.set(result)
        # After getting the result, we can start a new expression with it.
        expression = result
    except ZeroDivisionError:
        input_text.set("Error: Division by zero")
        expression = ""
    except Exception as e:
        input_text.set("Error: Invalid expression")
        expression = ""

def show_about_info():
    """
    This function is called when the about button is pressed.
    It displays an info message box.
    """
    messagebox.showinfo("About", "Tigray will Prevail")


# --- GUI Setup ---

# Create the main window for the calculator
window = tk.Tk()
window.title("Tigray Calculator")
window.geometry("375x650") # Set the size of the window
window.resizable(0, 0) # Make the window not resizable

# Global variable to store the expression
expression = ""

# StringVar to hold the text for the entry field
input_text = tk.StringVar()

# Create the frame for the input field
input_frame = tk.Frame(window, width=375, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
input_frame.pack(side=tk.TOP)

# Create the input field (entry widget) inside the frame
input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10) # Internal padding

# Create the frame for the buttons
btns_frame = tk.Frame(window, width=375, height=600, bg="grey")
btns_frame.pack()

# --- Button Layout ---
# We use grid layout for the buttons for precise placement.

# First row (Trigonometric and special functions)
sin_btn = tk.Button(btns_frame, text="sin", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: button_click('math.sin(')).grid(row=0, column=0, padx=1, pady=1)
cos_btn = tk.Button(btns_frame, text="cos", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: button_click('math.cos(')).grid(row=0, column=1, padx=1, pady=1)
tan_btn = tk.Button(btns_frame, text="tan", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: button_click('math.tan(')).grid(row=0, column=2, padx=1, pady=1)
pi_btn = tk.Button(btns_frame, text="π", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: button_click('math.pi')).grid(row=0, column=3, padx=1, pady=1)


# Second row
open_bracket_btn = tk.Button(btns_frame, text="(", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: button_click('(')).grid(row=1, column=0, padx=1, pady=1)
close_bracket_btn = tk.Button(btns_frame, text=")", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: button_click(')')).grid(row=1, column=1, padx=1, pady=1)
clear_btn = tk.Button(btns_frame, text="C", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: button_clear()).grid(row=1, column=2, padx=1, pady=1)
backspace_btn = tk.Button(btns_frame, text="⌫", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: button_backspace()).grid(row=1, column=3, padx=1, pady=1)


# Third row
seven_btn = tk.Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(7)).grid(row=2, column=0, padx=1, pady=1)
eight_btn = tk.Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(8)).grid(row=2, column=1, padx=1, pady=1)
nine_btn = tk.Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(9)).grid(row=2, column=2, padx=1, pady=1)
divide_btn = tk.Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#FFA500", cursor="hand2", command=lambda: button_click("/")).grid(row=2, column=3, padx=1, pady=1)

# Fourth row
four_btn = tk.Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(4)).grid(row=3, column=0, padx=1, pady=1)
five_btn = tk.Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(5)).grid(row=3, column=1, padx=1, pady=1)
six_btn = tk.Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(6)).grid(row=3, column=2, padx=1, pady=1)
multiply_btn = tk.Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#FFA500", cursor="hand2", command=lambda: button_click("*")).grid(row=3, column=3, padx=1, pady=1)

# Fifth row
one_btn = tk.Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(1)).grid(row=4, column=0, padx=1, pady=1)
two_btn = tk.Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(2)).grid(row=4, column=1, padx=1, pady=1)
three_btn = tk.Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(3)).grid(row=4, column=2, padx=1, pady=1)
subtract_btn = tk.Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#FFA500", cursor="hand2", command=lambda: button_click("-")).grid(row=4, column=3, padx=1, pady=1)

# Sixth row
zero_btn = tk.Button(btns_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(0)).grid(row=5, column=0, columnspan=2, padx=1, pady=1)
point_btn = tk.Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: button_click(".")).grid(row=5, column=2, padx=1, pady=1)
add_btn = tk.Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#FFA500", cursor="hand2", command=lambda: button_click("+")).grid(row=5, column=3, padx=1, pady=1)

# Seventh row
equals_btn = tk.Button(btns_frame, text="=", fg="black", width=42, height=3, bd=0, bg="#FFA500", cursor="hand2", command=lambda: button_equal()).grid(row=6, column=0, columnspan=4, padx=1, pady=1)

# Eighth row
about_btn = tk.Button(btns_frame, text="Tigray will Privail", fg="black", width=42, height=3, bd=0, bg="#eee", cursor="hand2", command=show_about_info).grid(row=7, column=0, columnspan=4, padx=1, pady=1)


# --- Start the main loop ---
# This line keeps the window open.
window.mainloop()
