# Turtle Graphics Game
import turtle
import math
import random
from random import randint
from turtle import Turtle

# Set Up Screen
wn = turtle.Screen()
wn.title("Maulana ID")
wn.bgcolor("black")

# Credits
def credits():
    turtle.color("white")
    turtle.speed(0)
    turtle.penup()
    turtle.setpos(-580, 200)
    turtle.write("Game Created\nBy Maulana ID", font=("Consolas", 20, "bold",))
    turtle.penup()
    turtle.hideturtle()
credits()

# Border
border = turtle.Turtle()
border.color("white")
border.penup()
border.setposition(-300, -300)
border.pendown()
border.pensize(3)
for side in range(4):
    border.forward(600)
    border.left(90)
border.hideturtle()
    
# Player
player = turtle.Turtle()
player.color("red")
player.shape("triangle")
player.penup()
player.speed(0)

# Goal
goal = turtle.Turtle()
goal.color("blue")
goal.shape("circle")
goal.penup()
goal.speed(0)
goal.setposition(random.randint(-290, 290), random.randint(-290,290))

# Speed
speed = 1
    
# Define Functions
def turnleft():
    player.left(30)

def turnright():
    player.right(30)

def boost():
    global speed
    speed += 1

def slow():
    global speed
    speed -= 1
    

# Set Control
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(boost, "Up")
turtle.onkey(slow, "Down")

while True:
    player.forward(speed)

    # Boundary Checking
    if player.xcor() > 300 or player.xcor() < -300:
        player.right(180)

    if player.ycor() > 300 or player.ycor() < -300:
        player.right(180)

    # Collision Checking
    d = math.sqrt(math.pow(player.xcor() - goal.xcor(),2) + math.pow(player.ycor() - goal.ycor(),2))
    if d < 20:
        goal.setposition(random.randint(-290, 290), random.randint(-290, 290))