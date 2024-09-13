import turtle


turtle.speed(1)
turtle.shape("turtle")

length = 100
turtle.forward(length)
turtle.left(90)
turtle.forward(length)
turtle.left(90)
turtle.forward(length)
turtle.left(90)
turtle.forward(length)

turtle.color("red")

turtle.backward(length)
turtle.penup()
turtle.right(90)
turtle.forward(length)
turtle.pendown()
turtle.circle(100)

turtle.mainloop()