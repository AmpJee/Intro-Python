import turtle

turtle.speed(100)
turtle.bgcolor("white")
turtle.shape("turtle")

 #face
turtle.goto(0, -150)
turtle.color("light grey")
turtle.begin_fill()
turtle.circle(150) 
turtle.end_fill()

#eyes
turtle.goto(60, 4)
turtle.color("black")
turtle.begin_fill()
turtle.circle(15)
turtle.end_fill()

turtle.penup()
turtle.goto(-60, 4)
turtle.color("black")
turtle.begin_fill()
turtle.circle(15)
turtle.end_fill()

#nose
turtle.goto(-6,-15)
turtle.pendown()
turtle.color("black")
turtle.begin_fill()
turtle.width(1)
turtle.forward(30)
turtle.right(140)
turtle.forward(30)
turtle.right(80)
turtle.forward(30)
turtle.right(140)
turtle.forward(30)
turtle.end_fill()

#mouth
turtle.width(4)
turtle.penup()
turtle.goto(-6,-15)
turtle.forward(30)
turtle.right(140)
turtle.forward(30)
turtle.pendown()
turtle.left(60)
turtle.circle(15, 120)

turtle.penup()
turtle.right(60)
turtle.goto(-6,-15)
turtle.forward(30)
turtle.right(140)
turtle.forward(50)
turtle.pendown()
turtle.left(120)
turtle.circle(15, 120)

#mustache
turtle.penup()
turtle.home()
turtle.goto(90, -15)
turtle.color("black")
turtle.width(2)
turtle.pendown()
turtle.left(30)
turtle.forward(80)
turtle.penup()

turtle.home()
turtle.goto(90, -25)
turtle.pendown()
turtle.forward(80)
turtle.penup()

turtle.home()
turtle.goto(90, -35)
turtle.pendown()
turtle.right(30)
turtle.forward(80)
turtle.penup()


turtle.home()
turtle.goto(-90, -35)
turtle.color("black")
turtle.width(2)
turtle.pendown()
turtle.left(30)
turtle.backward(80)
turtle.penup()

turtle.home()
turtle.goto(-90, -25)
turtle.pendown()
turtle.backward(80)
turtle.penup()

turtle.home()
turtle.goto(-90, -15)
turtle.pendown()
turtle.right(30)
turtle.backward(80)
turtle.penup()

#detail
turtle.home()
turtle.goto(-150, -250)
turtle.right(90)
turtle.pendown()
turtle.color("white")
turtle.begin_fill()
turtle.circle(150)
turtle.end_fill()
turtle.penup()

turtle.home()
turtle.goto(0, -150)
turtle.color("black")
turtle.width(1)
turtle.pendown()
turtle.circle(150) 
turtle.penup()


#white eyes
turtle.goto(57, 10)
turtle.color("white")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()
turtle.penup()

turtle.goto(-57, 10)
turtle.color("white")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()
turtle.penup()

#cheeks
turtle.home()
turtle.goto(65, -35)
turtle.color("pink")
turtle.begin_fill()
turtle.circle(12)
turtle.end_fill()
turtle.penup()

turtle.goto(-65, -35)
turtle.color("pink")
turtle.begin_fill()
turtle.circle(12)
turtle.end_fill()
turtle.penup()


turtle.hideturtle()
turtle.mainloop()
