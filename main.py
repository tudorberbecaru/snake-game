from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

WIDTH = 1500
HEIGHT = 900

# Set up the screen
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

# Initialize game components
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Set up key listeners for snake movement
screen.listen()
screen.onkeypress(snake.up, "w")
screen.onkeypress(snake.down, "s")
screen.onkeypress(snake.left, "a")
screen.onkeypress(snake.right, "d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)

    # Move the snake
    snake.move()

    # Check if snake has eaten the food
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Check for collision with walls
    if snake.head.xcor() > 750 or snake.head.xcor() < -750 or snake.head.ycor() > 450 or snake.head.ycor() < -450:
        scoreboard.reset_scoreboard()
        snake.reset_snake()

    # Check for collision with tail segments
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_scoreboard()
            snake.reset_snake()

screen.exitonclick()
