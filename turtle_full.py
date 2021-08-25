# Author        Alyk Skye
# Date          2021-05-26
# Revised       2021-05-27
# Version       03
# Filename      Gen_Py_Turtle_Template_03.py
# Description   Sample Python Turtle graphics template for
#               QUT Student Sucess Group - General Python modules
# _______	________

import turtle           # Allows the use of the turtle
import time             # Time delay functions

# Define all the funtions here
# ----------------------------

# Draw the multiple boxes on the canvas
def draw_boxes(size, spacing):

    # Draw square on the left
    green_turtle.goto(-(size + spacing), 0)     # Move turtle to start location
    green_turtle.showturtle()                   # Make turtle visible 
    draw_square(size)                           # Draw a box or four equal sides

    # Draw square on the right
    green_turtle.goto(100, 0)                   # Move turtle to start location
    draw_square(size)                           # Draw square on the right

    # Hide the green turtle
    green_turtle.hideturtle()
# End of draw_grid()

# Draw box to display text for user
def draw_box_title(size, horizontal, vertical):
    # Draw square on the left
    green_turtle.goto(horizontal, vertical)  # Move turtle to start location
    green_turtle.showturtle()               # Make turtle visible 
    green_turtle.pendown()
    
    # Draw a box of four equal sides in a clockwise direction
    green_turtle.setheading(0)
    for side in range(2):
      green_turtle.forward(size * 2)
      green_turtle.right(90)
      green_turtle.forward(size)
      green_turtle.right(90)
      
    green_turtle.penup()  
# End of draw_box_title()

def write_text(words, horizontal, vertical):
    
    green_turtle.goto(horizontal, vertical)
    green_turtle.color('black')
    green_turtle.write(words, align = 'center', font = ("times", 22, 'bold'))


# Draw a single square at the current top left corner
def draw_square(size):

    green_turtle.pendown()
    
    # Draw a box of four equal sides in a clockwise direction
    for side in range(4):
      green_turtle.forward(size)
      green_turtle.right(90)

    green_turtle.penup()  
# End of draw_square()

    

# Main program starts here
# ------------------------

# Control the size of the drawing space.
box_size = 70
box_spacing = 100
canvas_height = 400
canvas_width = 600
turtle_height = 1.0
turtle_width = 1.0

text_box_start = 180    # Start place for the text box
text_box_size = 160     # Dimension unit for user text box
text_increment = 30     # Spacing for next line of text
text_start = 140        # Vertical position of text to the user

drawing_delay = 1


# Sets the size for the turtle drawing.
turtle.setup(canvas_width, canvas_height)

# Create the place to use the turtle for drawing.
turtle_window = turtle.Screen()

# Set the title at the top of the window
turtle_window.title("QUT General Python")

red_turtle = turtle.Turtle()    # Create the red turtle
red_turtle.shape("turtle")
red_turtle.color("red")
red_turtle.hideturtle()

green_turtle = turtle.Turtle()    # Create the green turtle
green_turtle.shape("turtle")
green_turtle.color("green")
green_turtle.hideturtle()

blue_turtle = turtle.Turtle()    # Create the blue turtle
blue_turtle.shape("turtle")
blue_turtle.color("blue")
blue_turtle.hideturtle()

# Draw objects on the canvas using a user defined function.
green_turtle.penup()
green_turtle.goto(-120,130)
draw_box_title(text_box_size, -text_box_size, text_box_start)
draw_boxes(box_size, box_spacing)

# Say Hello to the user
write_text("Hello World", 0, text_start)
text_start -= text_increment

# Display the Red turtle in the left box.
red_turtle.penup()
red_turtle.goto(-(box_spacing + (box_size // 2)), -(box_size // 2))
red_turtle.setheading(180)
red_turtle.showturtle()
write_text("A Red Turtle", 0, text_start)
text_start -= text_increment

# A short delay.
time.sleep(drawing_delay)

# Hide the Red turtle then display the Blue turtle in the right box.
red_turtle.hideturtle()
blue_turtle.penup()
blue_turtle.goto((box_spacing + (box_size // 2)), -(box_size // 2))
blue_turtle.showturtle()
write_text("A Blue turtle", 0, text_start)
text_start -= text_increment

# A short delay.
time.sleep(drawing_delay)

# Change the shape of the two turtles.
red_turtle.shape("circle")
blue_turtle.shape("square")
write_text("Turtle shape change", 0, text_start)
text_start -= text_increment

# Using a loop make the circle and square turtles alternalte on the screen
for loop in range(2):
    # Increment the turtle width and height variables.
    turtle_width += 1
    turtle_height += 1

    # Adjust the Red turtle size, hide the Blue and show the Red
    red_turtle.shapesize(turtle_width, turtle_height, 1)
    blue_turtle.hideturtle()
    red_turtle.showturtle()

    # Short delay
    time.sleep(drawing_delay)
    
    # Adjust the Blue turtle size, hide the Red and show the Blue
    blue_turtle.shapesize(turtle_width, turtle_height, 1)
    red_turtle.hideturtle()
    blue_turtle.showturtle()

    # Short delay
    time.sleep(drawing_delay)



# Change the shape of the two turtles.
write_text("Turtle shape again", 0, text_start)
text_start -= text_increment

red_turtle.shape("turtle")
blue_turtle.shape("turtle")

red_turtle.setheading(0)
blue_turtle.setheading(180)

red_turtle.showturtle()
blue_turtle.showturtle()

green_turtle.goto(0, 0)
green_turtle.setheading(90)
green_turtle.showturtle()

# Draw all the code to the screen
turtle_window.mainloop()

# Exit the program

