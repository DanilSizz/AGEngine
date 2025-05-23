import math
import time

class Anim:
  
  def __init__(self, draw, objects):
    # Объект класса Draw
    self.draw = draw
    self.objects = objects
    
  def pulsing_circle(self, ball, speed = 1):
      
    ball.radius = (math.sin(time.time() * speed) + 1) * ball.startRadius
    #ball.y = ball.y - ball.radius / 2
    return ball

  # Функция для анимации объектов на экране
  def update_animations(self):
    self.draw.t.clear()
    # Добавляем анимацию пульсации шара
    self.objects[0] = self.pulsing_circle(self.objects[0], 1)
    self.objects[1] = self.pulsing_circle(self.objects[1], 2)
    self.draw.circle(self.objects[0])
    self.draw.circle(self.objects[1])
    self.draw.display.update_screen()