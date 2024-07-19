from turtle import  Screen                     # HI I AM HIMANSHU SHARMA
import time                                    # THIS IS MY FIRST SNAKE GAME
from food import food
from Snake import snake
from scoreboard import scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)

snake = snake()
food = food()
scoreboard=scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)

    snake.move()
    '''detection collision with food'''
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.increasescore()
    ''' detect collision with wall'''
    if snake.head.xcor() >280 or snake.head.xcor() <-280 or snake.head.ycor() >280 or snake.head.ycor() <-280 :
        game_is_on= False
        scoreboard.gameover()

    ''' detect collision with tail
    is head collide with any segment of snake 
    then we will trigger GAME OVER SEQUENCE'''
    for segments in snake.segments :
        if segments == snake.head:
            pass
        elif snake.head.distance(segments) < 10:
            game_is_on=False
            scoreboard.gameover()

screen.exitonclick()
