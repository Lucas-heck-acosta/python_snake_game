from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score
# setting up screen
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# initializing classes
snake = Snake()
food = Food()
score = Score()

# allowing for user input
screen.listen()
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")


def game_over():  # end game loop and call game over text
    global game_on
    score.gameover()
    game_on = False


game_on = True
# start game loop
while game_on:
    # set screen to update every .1 seconds
    screen.update()
    time.sleep(.1)
    # move snake forward
    snake.move()

    if snake.snake_segments[0].distance(food) <= 15:  # check for collision with food
        food.eat()
        score.point_up()
        snake.add_block()
        # delete current food, spawn a new one and increase snake size

    if snake.snake_segments[0].xcor() > 285 or snake.snake_segments[0].xcor() < -285 or snake.snake_segments[0].ycor() > 295 or snake.snake_segments[0].ycor() < -285:
        game_over()
        # setting game borders

    for seg in snake.snake_segments[1:]:
        if snake.snake_segments[0].distance(seg) < 10:  # check for collision with snake body
            game_over()
















screen.exitonclick()