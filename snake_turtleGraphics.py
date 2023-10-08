from turtle import Turtle, Screen
import time
import random

screen = Screen()
screen.setup(450, 650)
screen.bgcolor("gray")
screen.listen()
screen.tracer(0)
screen.title("SsSssnake")

playground = Turtle("square")
playground.offset = -100
playground.goto(0, playground.offset)
playground.color("black","green")
playground.shapesize(21)

apple = Turtle("circle")
apple.goto(0, -100)
apple.color("red")
apple.penup()
apple.goto((random.randint(-10, 10)*20), (random.randint(-10, 10)*20)+playground.offset)

head = Turtle("circle")
head.goto(0, +playground.offset)
head.penup()

score = Turtle()
score.penup()
score.hideturtle()
score.color("white")
score.highest_score = 0
score.actual_score = 0


'''------------------------MOVEMENT--------------------------'''

head.direction = "stop"

def move_up():
    if head.direction != "down" or len(body_parts) == 1:
        head.direction = "up"
def move_down():
    if head.direction != "up" or len(body_parts) == 1:
        head.direction = "down"
def move_left():
    if head.direction != "right" or len(body_parts) == 1:
        head.direction = "left"
def move_right():
    if head.direction != "left" or len(body_parts) == 1:
        head.direction = "right"
def move_stop():
    head.direction = "stop"


screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")
screen.onkeypress(move_stop, "space")

screen.onkeypress(move_up, "W")
screen.onkeypress(move_down, "S")
screen.onkeypress(move_left, "A")
screen.onkeypress(move_right, "D")

screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")


def move():
    if head.direction == "stop":
        head.goto(head.xcor(), head.ycor())
    elif head.direction == "up":
        head.goto(head.xcor(), head.ycor()+20)
    elif head.direction == "down":
        head.goto(head.xcor(), head.ycor()-20)
    elif head.direction == "left":
        head.goto(head.xcor()-20, head.ycor())
    elif head.direction == "right":
        head.goto(head.xcor()+20, head.ycor())

'''-------------------------------------------------------------'''

body_parts = [head]

def body_move():
    if head.direction != "stop":
        for index in range(len(body_parts)-1, 0, -1):
            body_parts[index].goto(body_parts[index-1].xcor(), body_parts[index-1].ycor())


def eat():
    if head.distance(apple) < 20:
        apple.goto((random.randint(-10, 10)*20),(random.randint(-10, 10)*20)+playground.offset)
        body = Turtle("square")
        body.penup()
        body_parts.append(body)
        score_inceament()
        apple_location_test()


def apple_location_test():
    for item in body_parts:
        if item.pos() == apple.pos():
            apple.goto((random.randint(-10, 10)*20),(random.randint(-10, 10)*20)+playground.offset)
            apple_location_test()


def self_colision():
    for item in body_parts[1::]:
        if item.pos() == head.pos():

            for _ in range(5):    

                for item in body_parts:
                    item.hideturtle()
                screen.update()
                time.sleep(.25)

                for item in body_parts:
                    item.showturtle()
                screen.update()
                time.sleep(.25)

            restart()


def restart():
    global body_parts

    for item in body_parts:
        item.goto(1000, 1000)
    body_parts.clear()
    body_parts = [head]
    head.goto(0, playground.offset)
    head.direction = "stop"

    apple.goto((random.randint(-10, 10)*20),(random.randint(-10, 10)*20)+playground.offset)

    score.actual_score = 0


def border_teleport():
    for item in body_parts:
        if item.xcor() < (-10*20):
            item.goto((item.xcor()*-1)-20, item.ycor())
        if item.xcor() > (10*20):
            item.goto((item.xcor()*-1)+20, item.ycor())
        if item.ycor() < (-10*20)+playground.offset:
            item.goto(item.xcor(), (10*20)+playground.offset)
        if item.ycor() > (10*20)+playground.offset:
            item.goto(item.xcor(), (-10*20)+playground.offset)


def score_rewrite():
    score.clear()
    score.goto(0, 265)
    score.write("Highest score:", font=("Verdana", 15, "normal"), align="center")
    score.goto(0, 220)
    score.write(score.highest_score, font=("Verdana", 25, "normal"), align="center")
    score.goto(0, 185)
    score.write("Actual score:", font=("Verdana", 15, "normal"), align="center")
    score.goto(0, 140)
    score.write(score.actual_score, font=("Verdana", 25, "normal"), align="center")


def score_inceament():
    score.actual_score += 5
    if score.actual_score > score.highest_score:
        score.highest_score = score.actual_score


while True:
    score_rewrite()
    eat()
    self_colision()
    body_move()
    move()
    border_teleport()
    screen.update()
    time.sleep(.15)


screen.exitonclick()