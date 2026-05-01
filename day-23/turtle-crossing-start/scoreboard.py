from turtle import Turtle
#Create a scoreboard that keeps track of which level the user is on. Every time the turtle
#player does a successful crossing, the level should increase. When the turtle hits a car,
#GAME OVER should be displayed in the center.


FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 0
        self.color("black")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-280, 250)
        self.write(f"Level: {self.level}", align="left", font=FONT)


    def add_level(self):
        self.level += 1
        self.update_scoreboard()
    def game_over(self):
        game_over = Turtle()
        game_over.color("black")
        game_over.penup()
        game_over.hideturtle()
        game_over.goto(0, 0)
        game_over.write("Game Over", align="center", font=FONT)
