from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Listener, KeyCode
import time

# Initialize the mouse controller
mouse = Controller()

# Variable to track the right Shift key state and click count
right_shift_pressed = False
click_count = 0

# Delay between clicks to achieve approximately 10 clicks per second (0.1 seconds)
click_delay = 0.1

# This function will be called when a key is pressed
def on_press(key):
    global right_shift_pressed
    if key == Key.shift_r:
        right_shift_pressed = True

# This function will be called when a key is released
def on_release(key):
    global right_shift_pressed
    global click_count

    if key == Key.shift_r:
        right_shift_pressed = False
        print(f"Total clicks while Shift was held down: {click_count}")
        click_count = 0

# Start the keyboard listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    while True:
        if right_shift_pressed:
            # Check if the left mouse button is pressed
            if mouse.position is not None:
                click_count += 1
                # Perform the left mouse click
                mouse.click(Button.left)
                # Add a delay between clicks
                time.sleep(click_delay)
