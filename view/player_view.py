import pygame
from booteroids.common import constants

class PlayerView:
  def draw(self, screen, player_polygon):
    pygame.draw.polygon(screen, constants.WHITE, player_polygon)
