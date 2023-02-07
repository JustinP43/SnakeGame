from turtle import Screen
import time
from food import Food
from snake import Snake 
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True

while game_is_on:
    screen.update()        
    time.sleep(.1)
    snake.move()
      
    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        
        check_food = True
        
        while check_food:
            fresh_location = True
            for segment in snake.segments:
                if food.position == segment.position:
                    fresh_location = False
            
            if fresh_location == True:
                check_food = False
            
                    
        
        snake.extend()
        scoreboard.increase_score()
        
    #Detect collision with wall 
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290 :
        scoreboard.gameover()
        game_is_on = False

    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.gameover()

    
screen.exitonclick()

