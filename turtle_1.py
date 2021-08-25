# Author        Alyk Skye
# Date          2021-07-17
# Revised       2021-07-19
# Variant       01.0
# Filename      Gen_Py_Turtle_Template_01-1.py
# Description   Sample Python Turtle graphics template for
#               QUT Student Sucess Group - General Python modules
# _______	________

import turtle           # Provides all functions for the turtle
import time             # Time delay functions


# User functions
# --------------

def green_turtle_move(): 

    # Create the green turtle
    green_turtle = turtle.Turtle()    
    green_turtle.shape("turtle")    # Set turtle shape
    green_turtle.color("green")     # Set turtle colour
    green_turtle.hideturtle()       # Make turtle invisable

    # Set parameters and show turtle
    green_turtle.goto(0, 0)         # Centre of the canvas
    green_turtle.setheading(90)     # Turn turtle upward
    green_turtle.showturtle()       # Make turtle visable
    green_turtle.stamp()            # Stamp a turtle shape

    # Short delay
    time.sleep(drawing_delay)

    # Change colour and thickness of the pen
    green_turtle.color("Orange")
    green_turtle.pensize(3)         # Increase line thickness

    # Move the turtle upwards
    green_turtle.forward(100)       # Move in the direction facing

    # Change turtle shape to a Red circle
    green_turtle.shape("circle")    # Change shape
    green_turtle.color("Red")       # Change colour
    green_turtle.stamp()            # Stamp a Red circle

    green_turtle.hideturtle()       # Become invisable


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
green_turtle_move()

# Draw all the code to the screen
turtle_window.mainloop()

# Exit the program

