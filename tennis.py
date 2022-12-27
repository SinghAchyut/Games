import turtle

wn = turtle.Screen()
wn.title("Tennis Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score1 = 0
score2 = 0

# Player 1
p1 = turtle.Turtle()
p1.speed(0)
p1.shape("square")
p1.color("blue")
p1.penup()
p1.goto(-350, 0)
p1.shapesize(stretch_wid=5, stretch_len=1)

# Player 2
p2 = turtle.Turtle()
p2.speed(0)
p2.shape("square")
p2.color("blue")
p2.penup()
p2.goto(+350, 0)
p2.shapesize(stretch_wid=5, stretch_len=1)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)

ball.dx = 0.2
ball.dy = -0.2
# ball.shapesize(stretch_wid=5, stretch_len=1)

# Pen 
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A : 0 Player B : 0", align="center", font=("Courier", 24, "normal"))
# Function 
def p1up() :
    y = p1.ycor()
    y += 30
    p1.sety(y)


def p1down() :
    y = p1.ycor()
    y -= 30
    p1.sety(y)

def p2up() :
    y = p2.ycor()
    y += 30
    p2.sety(y)


def p2down() :
    y = p2.ycor()
    y -= 30
    p2.sety(y)
# Bindings 
wn.listen()
wn.onkey(p1up, "w")
wn.onkey(p1down, "s")

wn.onkey(p2up, "Up")
wn.onkey(p2down, "Down")
# Main group loop

while True:
    wn.update()

    # moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # wall strikings
    if ball.ycor() > 290 :
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290 :
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390 :
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        pen.clear()
        pen.write("Player A : {} Player B : {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))


    if ball.xcor() < -390 :
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        pen.clear()
        pen.write("Player A : {} Player B : {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))


    # plyer collissions 
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < p2.ycor() + 40 and ball.ycor() > p2.ycor() - 40) :
        ball.dx *= -1

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < p1.ycor() + 40 and ball.ycor() > p1.ycor() - 40) :
        ball.dx *= -1