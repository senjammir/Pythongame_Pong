# Pong Game

import turtle
import os

wn = turtle.Screen()
wn.title("Pong by @SenJamir")
wn.bgcolor("grey")
wn.setup(width=800, height=600)
wn.tracer(0)  # stops window from updating. speeds up game

# Score
score_a = 0
score_b = 0


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # speed of animation to the maximum
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)  # speed of animation to the maximum
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)  # speed of animation to the maximum
ball.shape("square")
ball.color("black")
ball.penup()
ball.goto(0, 0)

ball.dx = 1.5  # everytime ball moves it moves by 1.5
ball.dy = -1.5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()  # no line when moving
pen.hideturtle()
pen.goto(0, 260)  # screen height is 600
pen.write("Player A: 0 . PlayerB: 0", align="center",
          font=("courier", 24, "normal"))

# Function


def paddle_a_up():  # function to move paddle a up
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():    # function to move paddle a down
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():  # function to move paddle b up
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():    # function to move paddle b down
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking/ball bounce
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1   # bounce down
        # add the & symbol to stop freeze when sound plays
        os.system("afplay bounce.wav&")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1   # bounce up
        os.system("afplay bounce.wav&")
    if ball.xcor() > 390:
        ball.goto(0, 0)     # ball goes back to 0 if it goes right
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} . PlayerB: {}".format(score_a, score_b),
                  align="center", font=("courier", 24, "normal"))
    if ball.xcor() < -390:
        ball.goto(0, 0)     # ball goes back to 0 if it goes right
        ball.dy *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} . PlayerB: {}".format(score_a, score_b),
                  align="center", font=("courier", 24, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor()) < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40:
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor()) < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40:
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")
