from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

##Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move the turtle north.
# If you get stuck, check the video walkthrough in Step 3.
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.go_to_start()
        self.moving_up = False
        self.moving_down = False

    def up(self):
        self.moving_up = True

    def stop_up(self):
        self.moving_up = False

    def move(self):
        if self.moving_up and self.ycor() < 281:
            self.sety(self.ycor() + MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
    def go_to_start(self):
        self.setposition(STARTING_POSITION)

