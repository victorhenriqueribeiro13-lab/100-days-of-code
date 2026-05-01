import time
from turtle import Screen
from player import Player
from car_manager import CarManager, MOVE_INCREMENT
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
turtle_player = Player()
car = CarManager()
scoreboard = Scoreboard()
screen.listen()

screen.onkeypress(turtle_player.up, "w")
screen.onkeyrelease(turtle_player.stop_up, "w")

# Generate a new car only every 6th time the game loop runs. If you get stuck, check the video walkthrough in Step 4.


counter = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    turtle_player.move()
    car.create_car_random_position()
    car.move_car()
    counter += 1
    if turtle_player.is_at_finish_line():
        turtle_player.go_to_start()
        scoreboard.add_level()
        scoreboard.update_scoreboard()
        car.level_up()

    for individual_car in car.all_cars:
        if turtle_player.distance(individual_car) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()


#Detect when the turtle player collides with a car and stop the game if this happens.








