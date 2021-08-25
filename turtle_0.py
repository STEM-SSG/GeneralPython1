# Author        Alyk Skye
# Date          2021-07-17
# Revised       2021-07-19
# Variant       01.0
# Filename      Gen_Py_Turtle_Template_01-0.py
# Description   Sample Python Turtle graphics template for
#               QUT Student Sucess Group - General Python modules
# _______	________

import turtle           # Allows the use of the turtle
import time             # Time delay functions


# User functions
# --------------



# Main program starts here
# ------------------------

# Control the size of the drawing space. Units are Pixels.
canvas_height = 400
canvas_width = 600

drawing_delay = 1       # Small delay for dramatic effect

# Setup the canvas for the turtle drawing.
turtle.setup(canvas_width, canvas_height)

# Create the place to use the turtle for drawing.
turtle_window = turtle.Screen()

# Set the title at the top of the window
turtle_window.title("QUT General Python Example 1")

# User instruction or functions to make turtle move


# Draw all the code to the screen
turtle_window.mainloop()

# Exit the program

