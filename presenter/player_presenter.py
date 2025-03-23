import math

class PlayerPresenter:
  def __init__(self):
    self._base_shape = [(0, -10), (5, 5), (-5, 5)]

  def present(self, player):
      
    cx, cy = player.x, player.y
    angle = player.angle
    points = []
    
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)

    for (bx, by) in self._base_shape:
        
      x = bx * cos_a - by * sin_a
      y = bx * sin_a + by * cos_a

      points.append((int(cx + x), int(cy + y)))
          
    return points
