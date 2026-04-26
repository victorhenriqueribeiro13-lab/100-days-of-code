import turtle
from turtle import Turtle, Screen
import random
#Turtle Race

screen = Screen()
screen.setup(width=700, height=600)
screen.bgcolor("black")
is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -55, -10, 35, 80, 125]
all_turtles = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[0])
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-330, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 320:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
                is_race_on = False
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
                is_race_on = False
        random_distance = random.randint(1, 10)
        turtle.forward(random_distance)









screen.exitonclick()
