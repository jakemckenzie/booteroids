import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

    self.rect = pygame.Rect(
      int(self.position.x - self.radius),
      int(self.position.y - self.radius),
      self.radius * 2,
      self.radius * 2
    )

  def draw(self, screen):
    pygame.draw.circle(screen, (255, 0, 0), (int(self.position.x), int(self.position.y)), self.radius, 2)
  
  def update(self, dt):
    self.position += self.velocity * dt
    self.rect.x = int(self.position.x - self.radius)
    self.rect.y = int(self.position.y - self.radius)

  def split(self):
    self.kill()

    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    
    random_angle = random.uniform(20, 50)

    new_velocity1 = self.velocity.rotate(random_angle) * 1.2
    new_velocity2 = self.velocity.rotate(-random_angle) * 1.2

    new_radius = self.radius - ASTEROID_MIN_RADIUS

    asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
    asteroid1.velocity = new_velocity1
        
    asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
    asteroid2.velocity = new_velocity2
  
  