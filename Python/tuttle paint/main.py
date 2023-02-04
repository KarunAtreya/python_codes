from turtle import Screen, Turtle

screen= Screen()
screen.bgcolor("black")


my_turtle= Turtle()
my_turtle.shape("square")
my_turtle.color("white")
for i in range(10):
    if i%2==0:
        my_turtle.penup()
        my_turtle.forward(10)
    else:
        my_turtle.forward(10)
    my_turtle.pendown()

screen.exitonclick()