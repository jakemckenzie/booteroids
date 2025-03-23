"""
Interactor layer for Game Flow.
Orchestrates the overall game logic, coordinating between Player, Asteroids, and Shots interactors.
Handles events like firing shots and detecting collisions, as well as overall game state (score, lives, game over).
"""
from booteroids.common import constants
from booteroids.interactor.player_interactor import PlayerInteractor
from booteroids.interactor.asteroid_interactor import AsteroidInteractor
from booteroids.interactor.shot_interactor import ShotsInteractor
import math

class GameInteractor:
  def __init__(self):
      
    self.player_interactor = PlayerInteractor()
    self.asteroid_interactor = AsteroidInteractor()
    self.shot_interactor = ShotsInteractor()
    
    self.score = 0
    self.lives = 3
    self.game_over = False
    self.wave = 1

    

  def fire_player_shot(self):
    px = self.player_interactor.player.x
    py = self.player_interactor.player.y
    angle = self.player_interactor.player.angle
    
    offset = 15
    
    fx = math.sin(angle) * offset
    fy = -math.cos(angle) * offset
    sx = px + fx
    sy = py + fy
    self.shot_interactor.fire_shot(sx, sy, angle)

  def update(self):
    if self.game_over:
      return
      
    self.player_interactor.update()
    self.asteroid_interactor.update()
    self.shot_interactor.update()
      
    ast_to_remove = []
    shot_to_remove = []
    for shot in list(self.shot_interactor.shots):
      for asteroid in list(self.asteroid_interactor.asteroids):
        
        dx = shot.x - asteroid.x
        dy = shot.y - asteroid.y
        
        if math.hypot(dx, dy) < (constants.SHOT_COLLISION_RADIUS + constants.ASTEROID_COLLISION_RADIUS):
            
          if asteroid not in ast_to_remove:
            ast_to_remove.append(asteroid)
            self.score += 10

          if shot not in shot_to_remove:
            shot_to_remove.append(shot)

      for asteroid in ast_to_remove:
        self.asteroid_interactor.remove_asteroid(asteroid)

      for shot in shot_to_remove:
        if shot in self.shot_interactor.shots:
          self.shot_interactor.shots.remove(shot)

      if len(self.asteroid_interactor.asteroids) == 0 and not self.game_over:
        self.wave += 1
        
        for _ in range(constants.ASTEROID_COUNT + self.wave - 1):
          self.asteroid_interactor.spawn_asteroid()
      
      for asteroid in list(self.asteroid_interactor.asteroids):
          
        dx = asteroid.x - self.player_interactor.player.x
        dy = asteroid.y - self.player_interactor.player.y

        if math.hypot(dx, dy) < (constants.PLAYER_COLLISION_RADIUS + constants.ASTEROID_COLLISION_RADIUS):
            
          self.lives -= 1
          
          if self.lives > 0:
            self.player_interactor.reset()
          else:
            self.game_over = True
          
          self.asteroid_interactor.remove_asteroid(asteroid)

          break
