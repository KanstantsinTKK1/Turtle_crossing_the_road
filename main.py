from turtle import Screen
from road import Road
from player import Player
from cars import Car
from score_level import Level
import time

game_is_on = True

screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)
screen.bgcolor(53, 56, 61)
screen.title('Turtle crosses the road')
screen.tracer(0)

road = Road()
road.paint_road()
some_cars = Car()
player = Player()
level = Level()
numbers_of_cars = 2
speed_cars = 0.1

screen.listen()
screen.onkey(fun=player.move_up_turtle, key='Up')
screen.onkey(fun=player.move_down_turtle, key='Down')


while game_is_on:
    time.sleep(speed_cars)
    some_cars.move_cars()
    some_cars.check_car()

    if numbers_of_cars != len(some_cars.list_cars):
        some_cars.add_car()

    if player.ycor() > 250:
        player.start_position()
        level.update_level()
        some_cars.traffic -= 0
        speed_cars *= 0.9
        numbers_of_cars += 1

    for car in some_cars.list_cars:
        if player.distance(car[0]) < 40:
            game_is_on = False
            level.game_over()

    screen.update()


screen.exitonclick()