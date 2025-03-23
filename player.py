import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self, *Player.containers)
    super().__init__(x, y, PLAYER_RADIUS)
    self.rotation = 0
    self.shoot_timer = 0.0


  def rotate(self, dt): 
    self.rotation += PLAYER_TURN_SPEED * dt
  
  def move(self, dt):
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    self.position += forward * PLAYER_SPEED * dt

  def triangle(self):
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * (self.radius / 1.5)

    a = self.position + forward * self.radius
    b = self.position - forward * self.radius - right
    c = self.position - forward * self.radius + right

    return [a, b, c]

  
  def draw(self, screen): 
    pygame.draw.polygon(screen, (255, 0, 0), self.triangle(), 2)

  def shoot(self):
    if self.shoot_timer <= 0:
      shot = Shot(self.position.x, self.position.y)
      shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
      self.shoot_timer = PLAYER_SHOOT_COOLDOWN

  def update(self, dt):
    self.shoot_timer = max(self.shoot_timer - dt, 0)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]: self.move(dt)
    if keys[pygame.K_s]: self.move(-dt)


    if keys[pygame.K_a]: self.rotation  += 180 * dt
    if keys[pygame.K_d]: self.rotation  -= 180 * dt

    if keys[pygame.K_SPACE]:
      self.shoot()