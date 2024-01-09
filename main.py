import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Slow and Steady Crossing")

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()

screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move()

    # Detecting collision with cars
    for cars in car.all_cars:
        if player.distance(cars) < 20:
            score.game_over()
            game_is_on = False

    # Detecting when player finishes
    if player.finish():
        player.start()
        car.level_up()
        score.update_score()

screen.exitonclick()
