from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()




screen.listen()
screen.onkeypress(r_paddle.Up, "Up")
screen.onkeypress(r_paddle.Down, "Down")

screen.onkeypress(l_paddle.Up, "w")
screen.onkeypress(l_paddle.Down, "s")

game_is_on = True

while game_is_on :
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()  

    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    if ball.distance(r_paddle) < 70 and ball.xcor() > 320 or ball.distance(l_paddle) < 70 and ball.xcor() < -320 :
        ball.bounce_x()    
        
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.restart()  
        time.sleep(0.5) 

    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.restart()  
        time.sleep(0.5)     
         


screen.exitonclick()