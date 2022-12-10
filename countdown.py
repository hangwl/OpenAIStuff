#!/usr/bin/env python

import tkinter as tk

# Create the main window
root = tk.Tk()

# Create a variable to store the time remaining
time_remaining = tk.IntVar()
time_remaining.set(10) # Set the initial time to 10 seconds

# Create a function to count down the time
def countdown():
    # Decrement the time remaining
    time_remaining.set(time_remaining.get() - 1)

    # If the time remaining is greater than 0,
    # run the function again after 1 second
    if time_remaining.get() > 0:
        root.after(1000, countdown)

# Create a function to start the countdown
def start_countdown():
    # Set the time remaining to the value entered in the input field
    time_remaining.set(int(time_input.get()))

    # Start the countdown
    countdown()

# Create a function to reset the countdown
def reset_countdown():
    # Set the time remaining to the initial time
    time_remaining.set(10)

# Create a label to display the time remaining
time_label = tk.Label(root, textvariable=time_remaining)
time_label.pack()

# Create an input field to enter the initial time
time_input = tk.Entry(root)
time_input.pack()

# Create a start button
start_button = tk.Button(root, text="Start", command=start_countdown)
start_button.pack()

# Create a reset button
reset_button = tk.Button(root, text="Reset", command=reset_countdown)
reset_button.pack()

# Run the main event loop
root.mainloop()

