import tkinter as tk
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Listener
import threading
import time

# Initialize the mouse controller
mouse = Controller()

# Variable to track the right Shift key state
right_shift_pressed = False

# Default delay between clicks to achieve approximately 10 clicks per second (0.1 seconds)
click_delay = 0.1
click_count = 0

# Function to continuously click at the specified rate
def click_continuously():
    global right_shift_pressed
    global click_count
    while True:
        if right_shift_pressed:
            # Check if the left mouse button is pressed
            if mouse.position is not None:
                # Perform the left mouse click
                mouse.click(Button.left)
                # Increment click count
                click_count += 1
                # Update the click_count_label
                window.after(1, update_click_count_label)
                # Add a delay between clicks
                time.sleep(click_delay)

# Function to update the click_count_label
def update_click_count_label():
    click_count_label.config(text="Number of clicks: " + str(click_count))

# Function to handle the right Shift key press and release to start/stop clicking
def on_key_press(key):
    global right_shift_pressed
    if key == Key.shift_r:
        right_shift_pressed = True

# Function to handle the right Shift key release to stop clicking
def on_key_release(key):
    global right_shift_pressed
    if key == Key.shift_r:
        right_shift_pressed = False

# Function to update the click delay based on the user input
def update_click_delay():
    global click_delay
    new_delay = click_delay_entry.get()
    try:
        click_delay = float(new_delay)
    except ValueError:
        pass

# Create the GUI window
window = tk.Tk()
window.title("AutoClicker")
window.geometry("300x150")

# Label and entry for setting the click delay
click_delay_label = tk.Label(window, text="Click Delay (seconds):")
click_delay_label.pack(pady=10)
click_delay_entry = tk.Entry(window)
click_delay_entry.pack(pady=5)
click_delay_entry.insert(0, str(click_delay))

# Submit button to apply the new click delay
submit_btn = tk.Button(window, text="Submit", command=update_click_delay)
submit_btn.pack(pady=5)

# Label to display the number of clicks
click_count_label = tk.Label(window, text="Number of clicks: " + str(click_count))
click_count_label.pack(pady=5)

# Bind the on_key_press and on_key_release functions to the keyboard listener
with Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    # Start the mouse click loop in a separate thread
    click_thread = threading.Thread(target=click_continuously)
    click_thread.start()

    # Start the GUI event loop
    window.mainloop()
