from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setposition(x=x, y=0)
        self.moving_up = False
        self.moving_down = False

    def up(self):
        self.moving_up = True

    def stop_up(self):
        self.moving_up = False

    def down(self):
        self.moving_down = True

    def stop_down(self):
        self.moving_down = False

    def move(self):
        if self.moving_up and self.ycor() < 250:
            self.sety(self.ycor() + 20)
        if self.moving_down and self.ycor() > -250:
            self.sety(self.ycor() - 20)