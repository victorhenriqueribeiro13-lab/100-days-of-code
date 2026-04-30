from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.dx = 6
        self.dy = 6
        self.move_speed = 0.1

    def move(self):
        self.setposition(self.xcor() + self.dx, self.ycor() + self.dy)

    def bounce_y(self):
        self.dy *= -1

    def bounce_x(self):
        self.dx *= -1
        self.dy *= 1.1
        self.dx *= 1.1
        self.move_speed *= 0.9

    def reset_position(self):
        self.setposition(0, 0)
        self.move_speed = 0.1
        self.dx = 6 if self.dx < 0 else -6
        self.dy = 6