#Библиотека time
import math

class Anim:
  
  def __init__(self, draw):
    #Объект класса Draw
    self.draw = draw
    
  def pulsing_circle(self, ball, speed = 1, step = 0.05):
      
      ball.radius = math.sin(ball.radius//2) * step

      return ball
         
  #Функция для анимации объектов на экране
  def update(self, ball):

    self.draw.setColor("Black")
    self.draw.setPenSize(10)
    self.draw.circle(ball)
    self.draw.display.update_screen() ###