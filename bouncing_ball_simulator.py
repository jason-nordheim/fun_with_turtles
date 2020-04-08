
import turtle

wn = turtle.Screen() 
wn.bgcolor("black")
wn.title("Bouncing ball simulator")

# ----------------
# Ball 
# ----------------
ball = turtle.Turtle()
ball.color("green")
ball.shape("circle")
ball.penup()
ball.speed(0) # remove default animations 
ball.goto(0,200)
ball.dy = -2 

# gravity = acceleration 
gravity = 0.15


while True:

  ball.dy -= gravity 
  ball.sety(ball.ycor() + ball.dy) 

  # check for bounce 
  if ball.ycor() < -300: 
    ball.dy *= -1 



wn.mainloop()   