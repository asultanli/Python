import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

starting_positions = [(0,0),(-20,0),(-40,0)]
segments = []

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.06)

    snake.snake_move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increse_score()
    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()
    # Detect collision with tail
    for segment in snake.segments[1::]:

        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()







screen.exitonclick()