import math

class ShotsPresenter:
   
  def __init__(self):
    base_shape = [(0,0), (12,0), (12,4), (4,4), (4,12), (0,12)]

    self._base_shape = [(x - 3, y - 3) for (x, y) in base_shape]

  def present(self, shots):
      
    shot_polygons = []
    for shot in shots:

      angle = shot.angle - (math.pi / 2)

      cos_a = math.cos(angle)
      sin_a = math.sin(angle)

      points = []

      for (bx, by) in self._base_shape:
          
          x = bx * cos_a - by * sin_a
          y = bx * sin_a + by * cos_a

          px = int((shot.x + x))
          py = int(shot.y + y)
          
          points.append((px, py))
          
      shot_polygons.append(points)
    return shot_polygons
