import random
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.cars=[]

    def create_car(self):
        if random.randint(1,6) == 1:
            car=Turtle()
            car.shape("square")
            car.color(random.choice(COLORS))
            car.penup()
            car.shapesize(stretch_len=2, stretch_wid=1)
            random_y= random.randint(-250,250)
            car.goto(300,random_y)
            self.cars.append(car)
            self.car_speed=STARTING_MOVE_DISTANCE

    def move_cars(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        self.car_speed+=MOVE_INCREMENT
