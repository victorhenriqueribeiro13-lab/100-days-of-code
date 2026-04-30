from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
r_paddle = Paddle(350)
l_paddle = Paddle(-350)

screen.onkeypress(l_paddle.up, "w")
screen.onkeyrelease(l_paddle.stop_up, "w")
screen.onkeypress(l_paddle.down, "s")
screen.onkeyrelease(l_paddle.stop_down, "s")



screen.onkeypress(r_paddle.up, "Up")
screen.onkeyrelease(r_paddle.stop_up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeyrelease(r_paddle.stop_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    r_paddle.move()
    l_paddle.move()

    # Colisão com parede
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Colisão com paddle direito
    if ball.dx > 0 and ball.xcor() > 320 and r_paddle.ycor() - 50 < ball.ycor() < r_paddle.ycor() + 50:
        ball.bounce_x()

    # Colisão com paddle esquerdo
    if ball.dx < 0 and ball.xcor() < -320 and l_paddle.ycor() - 50 < ball.ycor() < l_paddle.ycor() + 50:
        ball.bounce_x()

    # Bola saiu pela direita
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()




screen.exitonclick()