import pygame

class CircleShape(pygame.sprite.Sprite):
  
  def __init__(self, x, y, radius):
    if hasattr(self, "containers"):
      super().__init__(self.containers)
    else:
      super().__init__()
    
    self.position = pygame.Vector2(x, y)
    self.velocity = pygame.Vector2(0,0)

    self.radius = radius
  
  def draw(self, screen):
    raise NotImplementedError("Subclasses must override the draw method.")
  
  def update(self, dt):
    raise NotImplementedError("Subclasses must override the draw method.")
  
  def collides_with(self, other):
    distance = self.position.distance_to(other.position)
    return distance <= (self.radius + other.radius)