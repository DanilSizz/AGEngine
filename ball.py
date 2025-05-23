class Ball:
  
  def __init__(self, x, y, radius):
    self.x = x
    self.y = y
    self.startRadius = radius
    self.radius = radius
    
  def change_radius(self, step = 1,  multiplier = 1):
    self.radius += step * multiplier

  def getCoords(self):
    return [self.x, self.y]
