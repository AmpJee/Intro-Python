import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(1)

# Draw the head
t.penup()
t.goto(0, -50)
t.pendown()
t.circle(50)  # Head

# Draw the ears
t.penup()
t.goto(-30, 0)
t.pendown()
t.goto(-70, 80)  # Left ear
t.goto(-30, 0)

t.penup()
t.goto(30, 0)
t.pendown()
t.goto(70, 80)  # Right ear
t.goto(30, 0)

# Draw the body
t.penup()
t.goto(-25, -50)
t.pendown()
t.goto(-25, -150)  # Body left side
t.goto(25, -150)   # Body right side
t.goto(25, -50)

# Draw the legs
t.penup()
t.goto(-25, -150)
t.pendown()
t.goto(-50, -200)  # Left leg
t.goto(-25, -150)

t.penup()
t.goto(25, -150)
t.pendown()
t.goto(50, -200)   # Right leg
t.goto(25, -150)

# Draw the tail
t.penup()
t.goto(-25, -50)
t.pendown()
t.goto(-50, -70)   # Tail

# Finish
t.hideturtle()
turtle.done()

