from ..common import constants
import math

class Player:
  def __init__(self, start_x, start_y):
      
    self.x = start_x
    self.y = start_y
    self.angle = 0.0  # angle in radians, 0 pointing up
    self.vx = 0.0
    self.vy = 0.0

class PlayerInteractor:
  def __init__(self):
      
    start_x = constants.SCREEN_WIDTH / 2
    start_y = constants.SCREEN_HEIGHT / 2

    self.player = Player(start_x, start_y)

  def rotate_left(self):
    self.player.angle -= constants.PLAYER_ROTATION_SPEED

  def rotate_right(self):
    self.player.angle += constants.PLAYER_ROTATION_SPEED

  def thrust(self):
      
    ax = math.sin(self.player.angle)
    ay = -math.cos(self.player.angle)

    self.player.vx += ax * constants.PLAYER_THRUST
    self.player.vy += ay * constants.PLAYER_THRUST

  def update(self):
      
    self.player.x += self.player.vx
    self.player.y += self.player.vy

    if self.player.x < 0:
      self.player.x += constants.SCREEN_WIDTH
    elif self.player.x > constants.SCREEN_WIDTH:
      self.player.x -= constants.SCREEN_WIDTH
    if self.player.y < 0:
      self.player.y += constants.SCREEN_HEIGHT
    elif self.player.y > constants.SCREEN_HEIGHT:
      self.player.y -= constants.SCREEN_HEIGHT

  def reset(self):
      
    self.player.x = constants.SCREEN_WIDTH / 2
    self.player.y = constants.SCREEN_HEIGHT / 2

    self.player.vx = 0.0
    self.player.vy = 0.0
    self.player.angle = 0.0
