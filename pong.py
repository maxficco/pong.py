import turtle
import time
print("test")
print("vimtest")

wn = turtle.Screen()
wn.title("Max's Pong Game!")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.color("white")
paddleA.shape("square")
paddleA.shapesize(stretch_len=1, stretch_wid=5)
paddleA.penup()
paddleA.goto(-350, 0)

# Paddle B

paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.color("white")
paddleB.shape("square")
paddleB.shapesize(stretch_len=1, stretch_wid=5)
paddleB.penup()
paddleB.goto(350, 0)

# ball

ball = turtle.Turtle()
ball.speed(0)
ball.color("white")
ball.shape("circle") #Circle Instead??
ball.penup()
ball.goto(0, 0)
dx = 2.5
dy = 2.5

# pen
scoreA = 0
scoreB = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {}  Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))


# Functions
def paddle_a_up():
    if (paddleA.ycor() > 275):
        print("stopp")
    else:
        y = paddleA.ycor()
        y += 30
        paddleA.sety(y)

def paddle_a_down():
    if (paddleA.ycor() < -275):
        print("stopp")
    else:
        y = paddleA.ycor()
        y -= 30
        paddleA.sety(y)

def paddle_b_up():
    if (paddleB.ycor() > 275):
        print("stopp")
    else:
        y = paddleB.ycor()
        y += 30
        paddleB.sety(y)

def paddle_b_down():
    if (paddleB.ycor() < -275):
        print("stopp")
    else:
        y = paddleB.ycor()
        y -= 30
        paddleB.sety(y)

# Key Listeners
wn.listen()
wn.onkeypress(paddle_a_up, "a")
wn.onkeypress(paddle_a_down, "z")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
while True:

# moving the ball
    wn.update()
    ball.setx(ball.xcor() + dx)
    ball.sety(ball.ycor() + dy)
# collisions
    if ball.ycor() > 290:
        ball.sety(290)
        dy *= -1

    if ball.ycor() < -280:
        ball.sety(-280)
        dy *= -1

    if ball.xcor() > 380:
        ball.goto(0,0)
        dx *= 0
        dy *= 0
        scoreA += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))
        time.sleep(1)
        dx = -2
        dy = -2
    if ball.xcor() < -390:
        ball.goto(0,0)
        dx *= 0
        dy *= 0
        scoreB += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))
        time.sleep(1)
        dx = 2
        dy = 2

    if (ball.xcor() > 340 and ball.xcor() < 352.5) and (ball.ycor() < paddleB.ycor() + 49 and ball.ycor() > paddleB.ycor() - 49):
        dx *= -1
        ball.setx(340)
    if (ball.xcor() < -340 and ball.xcor() > -352.5) and (ball.ycor() < paddleA.ycor() + 49 and ball.ycor() > paddleA.ycor() - 49):
        dx *= -1
        ball.setx(-340)
    if scoreA == 10:
        pen.clear()
        pen.write("GAME OVER:  Player A Wins!", align="center", font=("Courier", 24, "normal"))
        dx = 0
        dy = 0
    if scoreB == 10:
        pen.clear()
        pen.write("GAME OVER:  Player B Wins!", align="center", font=("Courier", 24, "normal"))
        dx = 0
        dy = 0
