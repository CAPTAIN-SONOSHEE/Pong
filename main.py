from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()




screen.listen()
screen.onkeypress(r_paddle.Up, "Up")
screen.onkeypress(r_paddle.Down, "Down")

screen.onkeypress(l_paddle.Up, "w")
screen.onkeypress(l_paddle.Down, "s")

game_is_on = True

while game_is_on :
    time.sleep(0.1)
    screen.update()
    ball.move()


screen.exitonclick()