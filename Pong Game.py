import turtle as t 

TOTAL_POINTS = 5
playerAscore = 0
playerBscore = 0


window = t.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width=800,height=600)

playerAname = t.textinput("Player 1","Enter your name")
playerBname = t.textinput("Player 2","Enter your name")

#Creating left paddle
leftpaddle = t.Turtle()
leftpaddle.speed()
leftpaddle.color("white")
leftpaddle.shape("square")
leftpaddle.shapesize(stretch_len=1,stretch_wid=5)
leftpaddle.penup()
leftpaddle.goto(-350,0)

#Creating right paddle
rightpaddle = t.Turtle()
rightpaddle.speed()
rightpaddle.color("white")
rightpaddle.shape("square")
rightpaddle.shapesize(stretch_len=1,stretch_wid=5)
rightpaddle.penup()
rightpaddle.goto(350,0)

#creating a ball
ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(5,5)
ballxdirection = 5
ballydirection = 5

#creating variable for score update
pen = t.Turtle()
pen.speed()
pen.color("Blue")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score",align="center",font=('Arial',24,'normal'))

#moving the left paddle
def leftpaddleup():
    y = leftpaddle.ycor()
    if y < 250:  # To prevent moving out of the top border
        y += 30
        leftpaddle.sety(y)

def leftpaddledown():
    y = leftpaddle.ycor()
    if y > -240:  # To prevent moving out of the bottom border
        y -= 30
        leftpaddle.sety(y)

# Moving the right paddle
def rightpaddleup():
    y = rightpaddle.ycor()
    if y < 250:  # To prevent moving out of the top border
        y += 30
        rightpaddle.sety(y)

def rightpaddledown():
    y = rightpaddle.ycor()
    if y > -240:  # To prevent moving out of the bottom border
        y -= 30
        rightpaddle.sety(y)



window.listen()
window.onkeypress(leftpaddleup,'w')
window.onkeypress(leftpaddledown,'s')
window.onkeypress(rightpaddleup,'Up')
window.onkeypress(rightpaddledown,'Down')

while True:
    window.update()

    #moving the ball
    ball.setx(ball.xcor() + ballxdirection)
    ball.sety(ball.ycor() + ballydirection)

    if ball.ycor()>290:
        ball.sety(290)
        ballydirection = ballydirection * -1

    if ball.ycor()<-290:
        ball.sety(-290)
        ballydirection = ballydirection * -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ballxdirection *= -1  # Reverse direction
        playerAscore += 1
        pen.clear()
        pen.write(f"{playerAname}: {playerAscore}  {playerBname}: {playerBscore}", align='center', font=('Arial', 24, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ballxdirection *= -1  # Reverse direction
        playerBscore += 1
        pen.clear()
        pen.write(f"{playerAname}: {playerAscore}  {playerBname}: {playerBscore}", align='center', font=('Arial', 24, 'normal'))


    #handling the collisions
    if (350 > ball.xcor() > 340) and (rightpaddle.ycor() + 50 > ball.ycor() > rightpaddle.ycor() - 50):
        ball.setx(340)
        ballxdirection *= -1

    if (-350 < ball.xcor() < -340) and (leftpaddle.ycor() + 50 > ball.ycor() > leftpaddle.ycor() - 50):
        ball.setx(-340)
        ballxdirection *= -1
    
    #total points in the game
    if playerAscore == TOTAL_POINTS:
        pen.clear()
        pen.goto(0,0)
        ball.color("black")
        ball.goto(10,67)
        t.color("white")
        t.write(f"{playerAname} wins!",align="center", font=("Verdana",20,"bold"))
        break
        

    if playerBscore == TOTAL_POINTS:
        pen.clear()
        pen.goto(0,0)
        ball.color("black")
        ball.goto(10,67)
        t.color("white")
        t.write(f"{playerBname} wins!",align="center", font=("Verdana",20,"bold"))
        break


t.done()


