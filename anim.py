#Библиотека time
import time
import math

class Anim:
  
  def __init__(self, fps, draw):
    
    #Интервал обновления экрана
    self.interval = 1 / fps 
    #Таймер (объект класса Time)
    self.time = time.time()
    #Объект класса Draw
    self.draw = draw
    
  def pulsing_circle(self, ball, speed = 1, step = 0.05):
      
      ball.radius = math.sin(ball.radius//2) * step

      return ball
         
  #Функция для анимации объектов на экране
  def anim(self, ball):

    self.draw.setColor("red")
    self.draw.setPenSize(10)
    while True:
      
      elapsed_time = time.time() - self.time
  
      if elapsed_time < self.interval:
          time.sleep(self.interval - elapsed_time)
          
      print(ball.radius)
      #self.draw.screen.clear()
      self.pulsing_circle(ball)         
      self.draw.circle(ball)
      self.draw.display.update_screen() ###