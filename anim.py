import math
import time

class Anim:
  
  def __init__(self, draw, objects):
    # Объект класса Draw
    self.draw = draw
    self.objects = objects

  def movingCircle(self, ball, speed):
    ball.x = math.cos(time.time()  * speed) * ball.startRadius
    ball.y = math.sin(time.time()  * speed) * ball.startRadius
    return ball

  def pulsing_circle(self, ball, speed = 1):
      
    ball.radius = ball.startRadius + (math.sin(time.time() * speed) + 1) * ball.startRadius / 2

    return ball

  # Функция для анимации объектов на экране
  def update_animations(self):
    self.draw.t.clear()
    # Добавляем анимацию пульсации шара
    self.updateObjects()
    self.draw.display.update_screen()

  def updateObjects(self):
    self.draw.setNet()
    self.objects[0] = self.pulsing_circle(self.objects[0], 5)
    #self.objects[1] = self.pulsing_circle(self.objects[1], 2)
    self.objects[1] = self.movingCircle(self.objects[1], 5)
    self.draw.circle(self.objects[0])
    self.draw.circle(self.objects[1])