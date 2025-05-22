class Ball:
  
  def __init__(self, x, y, radius):
    self.x = x
    self.y = y
    self.radius = radius
    
  def change_radius(self, step = 1,  multiplier = 1):
    self.radius += step * multiplier
    
  
