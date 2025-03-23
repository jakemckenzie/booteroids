import pygame
from booteroids.common import constants

class ShotsView:
  def draw_all(self, screen, shots_polygons):
    for polygon in shots_polygons:
      pygame.draw.polygon(screen, constants.BROWN, polygon)
