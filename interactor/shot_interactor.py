from booteroids.common import constants
import math

class Shot:
  def __init__(self, x, y, angle):
    self.x = x
    self.y = y
    self.angle = angle
    self.vx = math.sin(angle) * constants.SHOT_SPEED
    self.vy = -math.cos(angle) * constants.SHOT_SPEED
    self.life = constants.SHOT_LIFETIME

class ShotsInteractor:
  def __init__(self):
    self.shots = []

  def fire_shot(self, x, y, angle):
    shot = Shot(x, y, angle)
    self.shots.append(shot)

  def update(self):
    for shot in list(self.shots):
      shot.x += shot.vx
      shot.y += shot.vy

      if shot.x < 0:
        shot.x += constants.SCREEN_WIDTH
      elif shot.x > constants.SCREEN_WIDTH:
        shot.x -= constants.SCREEN_WIDTH
      if shot.y < 0:
        shot.y += constants.SCREEN_HEIGHT
      elif shot.y > constants.SCREEN_HEIGHT:
        shot.y -= constants.SCREEN_HEIGHT

      shot.life -= 1
      if shot.life <= 0:
        self.shots.remove(shot)
