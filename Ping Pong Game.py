import turtle

# Create the window
wind = turtle.Screen()
wind.title("Ping Pong by Konker")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)

# Create the blue paddle
madrab1 = turtle.Turtle()
madrab1.speed(0)
madrab1.shape("square")
madrab1.color("blue")
madrab1.shapesize(stretch_wid=5, stretch_len=1)
madrab1.penup()
madrab1.goto(-360, 0)

# Create the red paddle
madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("red")
madrab2.shapesize(stretch_wid=5, stretch_len=1)
madrab2.penup()
madrab2.goto(360, 0)

# Create the ball
ball1 = turtle.Turtle()
ball1.speed(1)
ball1.shape("circle")
ball1.color("white")
ball1.penup()
ball1.goto(0, 0)
ball1.dx = 0.5
ball1.dy = 0.5

# Create the score display
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1: 0 Player 2: 0", align="center", font=("Courier", 24, "normal"))

# Function to move the blue paddle up
def madrab1_up():
    y = madrab1.ycor()
    y += 25
    madrab1.sety(y)

# Function to move the blue paddle down
def madrab1_down():
    y = madrab1.ycor()
    y -= 25
    madrab1.sety(y)

# Function to move the red paddle up
def madrab2_up():
    y = madrab2.ycor()
    y += 25
    madrab2.sety(y)

# Function to move the red paddle down
def madrab2_down():
    y = madrab2.ycor()
    y -= 25
    madrab2.sety(y)

# Register key bindings for paddle movement
wind.listen()
wind.onkeypress(madrab1_up, "w")
wind.onkeypress(madrab1_down, "s")
wind.onkeypress(madrab2_up, "Up")
wind.onkeypress(madrab2_down, "Down")

# Game loop
while True:
    wind.update()

    # Move the ball
    ball1.setx(ball1.xcor() + ball1.dx)
    ball1.sety(ball1.ycor() + ball1.dy)

    # Ball collision with top and bottom walls
    if ball1.ycor() > 290:
        ball1.sety(290)
        ball1.dy *= -1

    if ball1.ycor() < -290:
        ball1.sety(-290)
        ball1.dy *= -1

    # Ball collision with right and left walls
    if ball1.xcor() > 390:
        ball1.goto(0, 0)
        ball1.dx *= -1
        score1 += 1
        score.clear()
        score.write("Player 1: {} Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    if ball1.xcor() < -390:
        ball1.goto(0, 0)
        ball1.dx *= -1
        score2 += 1
        score.clear()
        score.write("Player 1: {} Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    # Ball collision with paddles
    if (ball1.xcor() > 340 and ball1.xcor() < 350) and (ball1.ycor() < madrab2.ycor() + 40 and ball1.ycor() > madrab2.ycor() - 40):
        ball1.setx(340)
        ball1.dx *= -1

    if (ball1.xcor() < -340 and ball1.xcor() > -350) and (ball1.ycor() < madrab1.ycor() + 40 and ball1.ycor() > madrab1.ycor() - 40):
        ball1.setx(-340)
        ball1.dx *= -1
        
# THE END OF THE GAME CODE. #
