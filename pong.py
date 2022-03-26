print("pong game")

import turtle
import winsound

wn = turtle.Screen()
wn.title("pong game by ofek lutzky")
wn.bgcolor("white")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score
score1 = 0
score2 = 0

#side 1 player
player1 = turtle.Turtle() #internal class
player1.speed(0) #speed of the animation not of the player
player1.shape("square")
player1.color("black")
player1.shapesize(stretch_wid=6, stretch_len=1)
player1.penup() # so it won't draw a line like pick up the pen from the paper
player1.goto(-350,0)


#side 2 player
player2 = turtle.Turtle() #internal class
player2.speed(0) #speed of the animation not of the player
player2.shape("square")
player2.color("black")
player2.shapesize(stretch_wid=6, stretch_len=1)
player2.penup() # so it won't draw a line like pick up the pen from the paper
player2.goto(350,0)


#ball
ball = turtle.Turtle() #internal class
ball.speed(0) #speed of the animation not of the player
ball.shape("square")
ball.color("black")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup() # so it won't draw a line like pick up the pen from the paper
ball.goto(0,0)
ball.xmove = 0.2 #the move of the ball will be in 2 pixels moves
ball.ymove = 0.2




#function go up player 1
def player1_up():
    y = player1.ycor()# the cordinate y strip of the player
    y += 20
    player1.sety(y)

def player1_down():
    y = player1.ycor()# the cordinate y strip of the player
    y -= 20
    player1.sety(y)

#function go up player 2
def player2_up():
    y = player2.ycor()# the cordinate y strip of the player
    y += 20
    player2.sety(y)

def player2_down():
    y = player2.ycor()# the cordinate y strip of the player
    y -= 20
    player2.sety(y)

#binding
wn.listen()
wn.onkeypress(player1_up,"w")
wn.onkeypress(player1_down,"s")
wn.onkeypress(player2_up,"Up")
wn.onkeypress(player2_down,"Down")

#uptade loop
points_player1 = 0 #the reset of the points
points_player2 = 0

#points
points = turtle.Turtle()
points.speed(0)
points.color("red")
points.penup()
points.hideturtle()
points.goto(0,260)
points.write("player1: 0   player2: 0", align="center", font=("Arial", 24, "bold"))


while True:
    wn.update()


    #mvoe the ball
    ball.setx(ball.xcor()+ball.xmove)
    ball.sety(ball.ycor() + ball.ymove)

    #border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.ymove *= -1


    if ball.ycor() < -290:
        ball.sety(-290)
        ball.ymove *= -1


    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.xmove *= -1
        points_player1+=1
        score1 += 1
        # number1.clear()
        points.clear()
        points.write("player1: {}   player2: {}".format(score1,score2), align="center", font=("Arial", 24, "bold"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.xmove *= -1
        points_player2+=1
        score2 += 1
        # number2.clear()
        points.clear()
        points.write("player1: {}   player2: {}".format(score1, score2), align="center", font=("Arial", 24, "bold"))

    #collisions
    if ball.xcor() > 340 and ball.xcor()<350 and (ball.ycor()< player2.ycor()+60 and ball.ycor()> player2.ycor()-60):
        ball.setx(340)
        ball.xmove *= -1
        winsound.PlaySound("Boing_sound_effect.WAV", winsound.SND_ASYNC) #unfortunetlly not reading the file, need to be original wav file
        # winsound.Beep(15000,1000) # very bad sound

    if ball.xcor() < -340 and ball.xcor()> -350 and (ball.ycor()< player1.ycor()+60 and ball.ycor()> player1.ycor()-60):
        ball.setx(-340)
        ball.xmove *= -1
        winsound.PlaySound("Boing_sound_effect.WAV", winsound.SND_ASYNC)





    # # player 1 points #my try to build points before the instruction
    # number1 = turtle.Turtle()
    # number1.speed(0)
    # number1.penup()
    # number1.goto(80, 260)
    # number1.write(points_player1, move=False, font=("Arial", 20, "bold"))
    # number1.hideturtle()
    #
    # # player 2 points
    # number2 = turtle.Turtle()
    # number2.speed(0)
    # number2.penup()
    # number2.goto(-80, 260)
    # number2.write(points_player2, move=False, font=("Arial", 20, "bold"))
    # number2.hideturtle()

    # print(player1.get_shapepoly()) # to see what is the shape size by pixels (saw that the shape size duplicate by 10)
