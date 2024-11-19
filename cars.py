from turtle import Turtle
import random
from types import new_class


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.list_cars = []
        self.traffic = 150


    def new_car(self, x_position, y_position):
        normal_distance = True
        for item in self.list_cars:
            if item[0].distance(x_position, y_position) < self.traffic:
                normal_distance = False
        if normal_distance:
            car = []
            body = Turtle(shape='square')
            body.penup()
            body.setheading(180)
            body.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
            body.shapesize(1.5, 3)
            body.goto(x_position,y_position)
            roof = Turtle(shape='square')
            roof.penup()
            roof.setheading(180)
            roof.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
            roof.shapesize(0.75, 1.5)
            roof.goto(x_position,y_position)
            car.append(body)
            car.append(roof)
            self.list_cars.append(car)



    def move_cars(self):
        for item in self.list_cars:
            item[0].forward(10)
            item[1].forward(10)


    def check_car(self):
        for car in self.list_cars:
            if car[0].xcor() < -330:
                x_position = random.randint(300, 600)
                y_position = random.randint(-180, 190)
                normal_distance = True
                for item in self.list_cars:
                    if item[0].distance(x_position,y_position) < self.traffic:
                        normal_distance = False
                if normal_distance:
                    car[0].goto(x_position, y_position)
                    car[1].goto(x_position, y_position)


    def add_car(self):
            x_position = random.randint(300, 600)
            y_position = random.randint(-180, 190)
            self.new_car(x_position, y_position)



