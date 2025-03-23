from booteroids.common import constants
import math, random

class Asteroid:
  def __init__(self, x, y, vx, vy, radius):
    self.x = x
    self.y = y
    self.vx = vx
    self.vy = vy
    self.radius = radius

class AsteroidInteractor:
  def __init__(self):
    self.asteroids = []
    
    for _ in range(constants.ASTEROID_COUNT):
      self.spawn_asteroid()

  def spawn_asteroid(self):
    while True:
      x = random.uniform(0, constants.SCREEN_WIDTH)
      y = random.uniform(0, constants.SCREEN_HEIGHT)
        
      dx = x - (constants.SCREEN_WIDTH / 2)
      dy = y - (constants.SCREEN_HEIGHT / 2)
      
      if math.hypot(dx, dy) > 100: break
          
      angle = random.uniform(0, 2 * math.pi)

      speed = random.uniform(constants.ASTEROID_SPEED_MIN, constants.ASTEROID_SPEED_MAX)

      vx = math.sin(angle) * speed
      vy = -math.cos(angle) * speed

      asteroid = Asteroid(x, y, vx, vy, constants.ASTEROID_RADIUS)

      self.asteroids.append(asteroid)

  def update(self):
    for asteroid in self.asteroids:
      asteroid.x += asteroid.vx
      asteroid.y += asteroid.vy
      if asteroid.x < 0:
        asteroid.x += constants.SCREEN_WIDTH
      elif asteroid.x > constants.SCREEN_WIDTH:
        asteroid.x -= constants.SCREEN_WIDTH
      if asteroid.y < 0:
        asteroid.y += constants.SCREEN_HEIGHT
      elif asteroid.y > constants.SCREEN_HEIGHT:
        asteroid.y -= constants.SCREEN_HEIGHT

  def remove_asteroid(self, asteroid):
      if asteroid in self.asteroids:
          self.asteroids.remove(asteroid)
