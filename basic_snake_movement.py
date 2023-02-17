# Import the Turtle Graphics module
import turtle

# Define program constants
WIDTH = 500
HEIGHT = 500
DELAY = 100

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

def go_up():
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"

def go_down():
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"

def go_right():
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"

def go_left():
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"

def game_loop():
    stamper.clearstamps()

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    #check collisions
    if new_head in snake or new_head[0] < -WIDTH/2 or new_head[0] > WIDTH/2\
        or new_head[1] < -HEIGHT/2 or new_head[1] > HEIGHT/2:
        turtle.bye()
    else:

        snake.append(new_head)

        snake.pop(0)

        for segment in snake:
            stamper.goto(segment[0], segment[1])
            stamper.stamp()

        screen.update()

        turtle.ontimer(game_loop, DELAY)

# Create a window where we will do our drawing.
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)  # Set the dimensions of the Turtle Graphics window.
screen.title("Snake")
screen.bgcolor("cyan")
screen.tracer(0)

#event handler
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")

# Create a turtle to do your bidding
stamper = turtle.Turtle()
stamper.shape("square")
stamper.penup()

#Create snake as coordinate pairs
snake = [[0,0], [20,0], [40,0], [60,0]]
snake_direction = "up"


#draw snake
for segment in snake:
    stamper.goto(segment[0], segment[1])
    stamper.stamp()

game_loop()

# This statement (or an equivalent) is needed at the end of all your turtle programs.
turtle.done()