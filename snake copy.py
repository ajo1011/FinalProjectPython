from random import randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
score = 0
obstacles = [vector(randrange(-15, 15) * 10, randrange(-15, 15) * 10) for _ in range(5)]  # Generate 5 random obstacles

score_writer = Turtle(visible=False)
score_writer.penup()
score_writer.goto(-190, 160)
score_writer.color('blue')

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y

def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

def display_score():
    score_writer.clear()
    score_writer.write(f"Score: {score}", font=("Arial", 14, "normal"))


def move():
    global score
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake or head in obstacles:
        square(head.x, head.y, 9, 'red')
        update()
        print("Game Over! Your score was:", score, font=("Arial", 14, "bold"))
        return

    snake.append(head)

    if head == food:
        score += 10  # Increase score by 10 for each food eaten
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    for obstacle in obstacles:
        square(obstacle.x, obstacle.y, 9, 'brown')  # Draw obstacles in brown

    square(food.x, food.y, 9, 'green')
    display_score()  # Update score display after each move
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
