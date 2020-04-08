# Simple pong game 
# originally by @TokyoEdTech 

import turtle
BUFFER = 10 
MOVE_DISTANCE = 20 
BOARD_HEIGHT = 600
BOARD_WIDTH = 800
RIGHT_EDGE = (BOARD_WIDTH / 2) - BUFFER
LEFT_EDGE = (BOARD_WIDTH / 2 * -1) + BUFFER
TOP_EDGE = (BOARD_HEIGHT / 2) - BUFFER
BOTTOM_EDGE = (BOARD_HEIGHT / 2 * -1) + BUFFER
PADDLE_WIDTH = 5
PADDLE_LENGTH = 1 

# definte the window 
wn = turtle.Screen()
wn.title("Pong by Jason Nordheim")
wn.bgcolor("black")
wn.setup(width=BOARD_WIDTH,height=BOARD_HEIGHT)
wn.tracer(0)

# paddle a 
paddle_a = turtle.Turtle() 
paddle_a.speed(0) # speed of animation - sets the speed to the maximum possible speed. 
paddle_a.shape("square") # there are a few built in shapes 
paddle_a.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_LENGTH)
paddle_a.color("white") # assign the color 
paddle_a.penup() 
paddle_a.goto(-350,0)

# paddle b 
paddle_b = turtle.Turtle() 
paddle_b.speed(0) # speed of animation - sets the speed to the maximum possible speed. 
paddle_b.shape("square") # there are a few built in shapes 
paddle_b.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_LENGTH)
paddle_b.color("white") # assign the color 
paddle_b.penup() 
paddle_b.goto(350,0)

# ball (defaults to 10 x 10)
ball = turtle.Turtle() 
ball.speed(0) # speed of animation - sets the speed to the maximum possible speed. 
ball.shape("square") # there are a few built in shapes 
ball.color("white") # assign the color 
ball.penup() 
ball.goto(0,0)
ball.dx = 2 
ball.dy = -2



#######################
# functions 
#######################
def paddle_a_up():
    # get the y cordinate, y should increase as it goes up 
    y = paddle_a.ycor() 
    y += MOVE_DISTANCE
    paddle_a.sety(y) 

def paddle_a_down():
    # get the y cordinate, y should decrease as it goes up 
    y = paddle_a.ycor() 
    y -= MOVE_DISTANCE
    paddle_a.sety(y) 

def paddle_b_up():
    # get the y cordinate, y should increase as it goes up 
    y = paddle_b.ycor() 
    y += MOVE_DISTANCE
    paddle_b.sety(y) 

def paddle_b_down():
    # get the y cordinate, y should decrease as it goes up 
    y = paddle_b.ycor() 
    y -= MOVE_DISTANCE
    paddle_b.sety(y) 

# instruct the computer to listen 
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

#######################
# main game loop 
#######################
while True:
    wn.update()

    # move the ball 
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # top border 
    # ball checking - hit wall and bounce 
    if ball.ycor() > TOP_EDGE: 
        ball.sety(TOP_EDGE)
        ball.dy *= -1
    
    # ball checking - hit wall and bounce 
    # bottom border 
    if ball.ycor() < BOTTOM_EDGE: 
        ball.sety(BOTTOM_EDGE)
        ball.dy *= -1
    
    # if the balls goes off the right side of the screen
    if(ball.xcor() > RIGHT_EDGE):
        ball.goto(0,0)
        ball.dx *= -1 

    # if the balls goes off the left side of the screen
    if(ball.xcor() < LEFT_EDGE):
        ball.goto(0,0)
        ball.dx *= -1 

    # paddle and ball collisions 
    # check if ball is contacting the paddle 
    # between the top and bottom portions of the paddle 
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1 
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1 
