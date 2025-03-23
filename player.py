import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot
from wrap import wrap_position

class Player(CircleShape):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self, *Player.containers)
    super().__init__(x, y, PLAYER_RADIUS)
    self.rotation = 0
    self.shoot_timer = 0.0

    self.base_image = pygame.image.load("assets/boots.png").convert_alpha()

    scale_factor = (self.radius * 2) / self.base_image.get_width() 
    
    new_width  = int(2 *self.base_image.get_width()  * scale_factor)
    new_height = int(2 * self.base_image.get_height() * scale_factor)


    self.base_image = pygame.transform.scale(self.base_image, (new_width, new_height))

    self.width = new_width
    self.height = new_height

    self.rect = self.base_image.get_rect(center=(int(self.position.x), int(self.position.y)))

  def rotate(self, dt): 
    self.rotation += PLAYER_TURN_SPEED * dt

  
  def draw(self, screen): 
    # Rotates boots by -self.rotation to give you the proper boots field
    rotated_image = pygame.transform.rotate(self.base_image, -self.rotation)

    # If your "forward" vector is (0, 1) with self.rotation rotated onto it, 
    # that usually is rotating clockwise within screen space. 
    # pygame.transform.rotate(surface, angle) actually turns images counterclockwise, 
    # though. Omitting the rotation angle or subtracting the rotation angle makes it 
    # stay correct with your present direction logic.
    rect = rotated_image.get_rect()
    rect.center = (self.position.x, self.position.y)

    screen.blit(rotated_image, rect)

  def shoot(self):
    if self.shoot_timer <= 0:
      shot = Shot(self.position.x, self.position.y)
      shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
      self.shoot_timer = PLAYER_SHOOT_COOLDOWN

  def update(self, dt):
    self.shoot_timer = max(self.shoot_timer - dt, 0)

    keys = pygame.key.get_pressed()

    forward = pygame.Vector2(0, 1).rotate(self.rotation)

    if keys[pygame.K_w]: self.velocity += forward * PLAYER_ACCELERATION * dt
    if keys[pygame.K_s]: self.velocity -= forward * PLAYER_ACCELERATION * dt

    self.velocity *= (1 - PLAYER_FRICTION * dt)

    self.position += self.velocity * dt

    if keys[pygame.K_a]: self.rotation  += PLAYER_TURN_SPEED  * dt
    if keys[pygame.K_d]: self.rotation  -= PLAYER_TURN_SPEED  * dt

    if keys[pygame.K_SPACE]:
      self.shoot()
    self.position = wrap_position(self.position, SCREEN_WIDTH, SCREEN_HEIGHT)