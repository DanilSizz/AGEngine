import turtle
import display

class Draw:
  
  def __init__(self):
    self.t = turtle.Turtle()
    self.t.hideturtle()
    self.display = display.Display(500, 500, 60)
    self.display.screen.tracer(0)

  def setColor(self, color = "BLACK"):
    self.t.color(color)

  def setPenSize(self, size):
    self.t.pensize(size)
    
  def teleport(self, x, y):
    self.t.penup()
    self.t.goto(x, y)
    self.t.pendown()
  
  def circle(self, ball, fill = False):

    if (fill):
      self.t.begin_fill()
      
    self.teleport(ball.x, ball.y - ball.radius / 2)
    self.t.circle(ball.radius)

    if (fill):
      self.t.end_fill()