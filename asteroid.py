import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH
from wrap import wrap_position

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

    asteroid_images = ["badcop.png", "lane.png", "prime.png", "teej.png", "trshpuppy.png"]

    chosen_image = random.choice(asteroid_images)

    self.base_image = pygame.image.load(chosen_image).convert_alpha()

    new_size = (int(self.radius * 2), int(self.radius * 2))
    self.image = pygame.transform.scale(self.base_image, new_size)

    self.rect = self.image.get_rect(center=(int(self.position.x), int(self.position.y)))

  def draw(self, screen):
    self.rect.center = (int(self.position.x), int(self.position.y))
    screen.blit(self.image, self.rect)
  
  def update(self, dt):
    self.position += self.velocity * dt
    self.rect.x = int(self.position.x - self.radius)
    self.rect.y = int(self.position.y - self.radius)
    self.position = wrap_position(self.position, SCREEN_WIDTH, SCREEN_HEIGHT)

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
  
  