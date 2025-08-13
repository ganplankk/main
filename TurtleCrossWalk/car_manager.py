from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        # super().__init__()
        # self.color = COLORS
        # self.penup()
        # self.shape("square")
        # self.create_car()
        # self.shapesize(1,3,5)
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_change = random.randint(1,6)
        if random_change == 1:
            new_car = Turtle("square")
            new_car.shapesize(1,2,5)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def car_move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
        # if level != 0:
        #     for car in self.all_cars:
        #         new_x = car.xcor() - MOVE_INCREMENT
        #         car.goto(new_x, car.ycor())
        # else:
        #     for car in self.all_cars:
        #         new_x = car.xcor() - STARTING_MOVE_DISTANCE
        #         car.goto(new_x, car.ycor())


    def car_speed_up(self):
        self.car_speed += MOVE_INCREMENT